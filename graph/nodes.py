import json
import logging
import os
import sys
import time
from typing import Literal

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage
from langgraph.types import interrupt, Command
from langgraph.graph import END

from graph.state import DDState
from graph.loader import load_docs_from_path
from graph.embeddings_store import build_or_load_vectorstore, retrieve_for_stage
from graph.stages import get_stages

load_dotenv()

log = logging.getLogger(__name__)

MODEL = "gemini-2.5-flash"

# ANSI codes used inside nodes for inline stream formatting
_RESET = "\033[0m"
_DIM   = "\033[2m"
_BOLD  = "\033[1m"
_GREEN = "\033[32m"
_RED   = "\033[31m"

SYSTEM_PROMPT = """You are a senior investment analyst conducting institutional-grade due diligence.
You follow a strict gated process. You are analytical, skeptical, and concise.
You never speculate beyond what the documents support.
You MUST return ONLY a valid JSON object — no markdown, no commentary, no code fences."""

STAGE_PROMPT_TEMPLATE = """## DEAL: {deal_type}
## {stage_name}

### OBJECTIVE
{objective}

### CHECKLIST
{checklist}

### KILL CRITERIA
{kill_criteria}

---
### RETRIEVED CONTEXT (semantically relevant excerpts from the dataroom)
{docs_content}

---
### INSTRUCTIONS
Using ONLY the retrieved context above, return a single JSON object with this exact schema
(no markdown fences, no extra keys, no trailing text):

{{
  "checklist_findings": [
    {{
      "item": "<checklist item text>",
      "finding": "<your analysis, max 80 words>",
      "sources": ["<filename>"],
      "sufficient": true | false
    }}
  ],
  "kill_criteria_results": [
    {{
      "criterion": "<criterion text>",
      "triggered": true | false,
      "reasoning": "<1-2 sentences>"
    }}
  ],
  "summary": "<overall stage summary, max {max_words} words>",
  "gate_decision": "GO" | "NO_GO",
  "gate_reasoning": "<one sentence explaining the gate decision>"
}}

Rules:
- Set gate_decision to NO_GO if ANY kill criterion is triggered
- Set triggered=true only when the criterion clearly applies based on document evidence
- sources must be real filenames from the context, not invented
- sufficient=false when the context is silent on a checklist item"""


def _build_prompt(deal_type: str, stage: dict, retrieved_context: str) -> list:
    checklist_str = "\n".join(f"  - {item}" for item in stage["checklist"])
    kill_str = (
        "\n".join(f"  ❌ {item}" for item in stage["kill_criteria"])
        if stage["kill_criteria"]
        else "  (No automatic kill criteria for this stage)"
    )

    user_content = STAGE_PROMPT_TEMPLATE.format(
        deal_type=deal_type.upper(),
        stage_name=stage["name"],
        objective=stage["objective"],
        checklist=checklist_str,
        kill_criteria=kill_str,
        docs_content=retrieved_context,
        max_words=stage["max_words"],
    )

    return [
        SystemMessage(content=SYSTEM_PROMPT),
        HumanMessage(content=user_content),
    ]


def _parse_structured_output(raw: str) -> dict:
    """Strip markdown fences if present and parse JSON. Falls back to a minimal dict."""
    text = raw.strip()
    # Strip ```json ... ``` or ``` ... ``` fences
    if text.startswith("```"):
        lines = text.splitlines()
        text = "\n".join(lines[1:-1] if lines[-1].strip() == "```" else lines[1:])
    try:
        return json.loads(text)
    except json.JSONDecodeError as e:
        log.warning("JSON parse failed (%s) — storing raw output as summary", e)
        return {
            "checklist_findings": [],
            "kill_criteria_results": [],
            "summary": raw,
            "gate_decision": _parse_gate_fallback(raw),
            "gate_reasoning": "(parse error — raw text stored in summary)",
        }


def _parse_gate_fallback(response_text: str) -> str:
    """Last-resort gate extraction from plain text."""
    upper = response_text.upper()
    if "NO_GO" in upper or "NO-GO" in upper:
        return "NO_GO"
    return "GO"


def _build_llm(stage: dict) -> ChatGoogleGenerativeAI:
    """
    Build a per-stage LLM with:
    - max_output_tokens computed from the stage's actual full-JSON content budget
    - thinking_budget=0  to disable Gemini 2.5 reasoning tokens (structured JSON
      extraction does not benefit from chain-of-thought, and reasoning tokens are
      billed and counted on top of content tokens)

    Budget formula:
        ~112 tokens per checklist finding  (80 words × 1.4 tok/word)
        ~56  tokens per kill-criterion     (40 words × 1.4 tok/word)
        max_words × 1.4  for the summary
        + 200 fixed overhead (JSON keys, gate_decision, gate_reasoning fields)
        × 1.3 safety buffer
    """
    n_check = len(stage["checklist"])
    n_kill  = len(stage.get("kill_criteria", []))
    raw = (
        n_check * 112
        + n_kill  *  56
        + int(stage["max_words"] * 1.4)
        + 200
    )
    max_output_tokens = int(raw * 1.3)

    return ChatGoogleGenerativeAI(
        model=MODEL,
        temperature=0,
        google_api_key=os.environ["GEMINI_API_KEY"],
        max_output_tokens=max_output_tokens,
        thinking_budget=0,
    )


# ─── Node: load_docs ──────────────────────────────────────────────────────────

def load_docs(state: DDState) -> dict:
    log.info("Node load_docs — path: %s", state["docs_path"])
    docs = load_docs_from_path(state["docs_path"])
    log.info("Node load_docs complete — %d doc(s) ready", len(docs))
    return {"raw_docs": docs}


# ─── Node: embed_docs ────────────────────────────────────────────────────────

def embed_docs(state: DDState) -> dict:
    log.info("Node embed_docs — building / loading vector store")
    _, persist_dir = build_or_load_vectorstore(state["docs_path"], state["raw_docs"])
    log.info("Node embed_docs complete — store at %s", persist_dir)
    return {"embeddings_path": persist_dir}


# ─── Node: run_stage ─────────────────────────────────────────────────────────

def run_stage(state: DDState) -> dict:
    stages  = get_stages(state["deal_type"])
    current = state["current_stage"]
    total   = len(stages)

    if current >= total:
        log.info("All %d stages complete.", total)
        return {"final_status": "completed"}

    stage = stages[current]

    log.info("┌─ Stage %d/%d  —  %s", current + 1, total, stage["name"])
    log.info("│  Objective    : %s", stage["objective"])
    log.info("│  Max words    : %d  |  Kill criteria : %d",
             stage["max_words"], len(stage["kill_criteria"]))

    # ── Retrieve relevant context from vector store ───────────────────────
    retrieved_context = retrieve_for_stage(state["embeddings_path"], stage)
    context_chars     = len(retrieved_context)
    log.info("│  RAG context  : %d chars  (~%d tokens)", context_chars, context_chars // 4)
    log.info("└─ Streaming from %s ...\n", MODEL)

    messages = _build_prompt(state["deal_type"], stage, retrieved_context)
    llm      = _build_llm(stage)
    log.info("│  Token budget : max_output=%d  thinking=off", llm.max_output_tokens or 0)

    # ── Live token stream ────────────────────────────────────────────────
    print(f"{_DIM}{'─' * 72}{_RESET}", flush=True)
    print(f"{_DIM}  [waiting for first token...]{_RESET}", end="", flush=True)

    t0            = time.perf_counter()
    full_response = ""
    first_token   = True
    usage_chunk   = None   # first chunk that carries usage_metadata

    try:
        for chunk in llm.stream(messages):
            if chunk.usage_metadata and usage_chunk is None:
                usage_chunk = chunk
            token = chunk.content
            if token:
                if first_token:
                    print(f"\r{' ' * 40}\r", end="", flush=True)
                    first_token = False
                sys.stdout.write(token)
                sys.stdout.flush()
                full_response += token
    except Exception as exc:
        print()
        log.error("LLM stream error at stage %d: %s", current + 1, exc)
        raise

    elapsed = time.perf_counter() - t0
    print(f"\n{_DIM}{'─' * 72}{_RESET}\n", flush=True)
    # ── End stream ──────────────────────────────────────────────────────

    # ── Token counts ────────────────────────────────────────────────────
    input_tokens  = 0
    output_tokens = 0

    if usage_chunk:
        um = usage_chunk.usage_metadata  # always non-None here
        input_tokens  = um.get("input_tokens", 0)
        output_tokens = um.get("output_tokens", 0)
    log.info(
        "Stage %d/%d  tokens  in=%d  out=%d  total=%d  elapsed=%.1fs",
        current + 1, total, input_tokens, output_tokens,
        input_tokens + output_tokens, elapsed,
    )

    # ── Parse structured JSON output ─────────────────────────────────────
    structured = _parse_structured_output(full_response)
    gate        = structured.get("gate_decision", "GO").upper()
    if gate not in ("GO", "NO_GO"):
        gate = _parse_gate_fallback(full_response)

    next_stage = current + 1
    is_last    = next_stage >= total

    gate_colour = _GREEN if gate == "GO" else _RED
    log.info(
        "Stage %d/%d complete  %.1fs  →  GATE: %s%s%s",
        current + 1, total, elapsed,
        gate_colour + _BOLD, gate, _RESET,
    )

    result = {
        "stage":         current,
        "name":          stage["name"],
        "output":        structured,       # structured JSON dict
        "gate_decision": gate,
        "input_tokens":  input_tokens,
        "output_tokens": output_tokens,
    }

    if gate == "NO_GO":
        final_status = "killed"
        log.warning("NO_GO triggered — deal killed at stage %d/%d", current + 1, total)
    elif is_last:
        final_status = "completed"
        log.info("Final stage passed — deal advanced to IC.")
    else:
        final_status = "in_progress"

    return {
        "stage_results":       [result],
        "current_stage":       next_stage,
        "gate_decision":       gate,
        "final_status":        final_status,
        "total_input_tokens":  input_tokens,
        "total_output_tokens": output_tokens,
    }


# ─── Node: human_gate ────────────────────────────────────────────────────────

def human_gate(state: DDState) -> Command:
    """
    Interrupts the graph to ask the human for a GO / NO_GO decision.
    On resume the interrupt() call returns the human's decision string.
    NOTE: on resume this node restarts from the top — interrupt() must be first.
    """
    stages      = get_stages(state["deal_type"])
    current     = state["current_stage"]   # already incremented by run_stage
    total       = len(stages)
    last_result = state["stage_results"][-1]

    # ── Pause and surface stage info to the CLI ──────────────────────────────
    user_decision: str = interrupt({
        "stage_name": last_result["name"],
        "llm_gate":   last_result["gate_decision"],
        "stage":      current,
        "total":      total,
    })
    # ── Resume: user_decision is "GO" or "NO_GO" ─────────────────────────────

    is_last = current >= total

    log.info(
        "human_gate  stage %d/%d  user=%s  is_last=%s",
        current, total, user_decision, is_last,
    )

    if user_decision == "NO_GO":
        return Command(
            update={"gate_decision": "NO_GO", "final_status": "killed"},
            goto=END,
        )
    elif is_last:
        return Command(
            update={"gate_decision": "GO", "final_status": "completed"},
            goto=END,
        )
    else:
        return Command(
            update={"gate_decision": "GO", "final_status": "in_progress"},
            goto="run_stage",
        )
