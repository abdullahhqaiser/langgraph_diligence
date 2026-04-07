"""
Due Diligence CLI — MVP

Usage:
    python main.py <deal_type> <docs_path>

Examples:
    python main.py biotech test_docs/biotech
    python main.py mature_mbo test_docs/mature_mbo
    python main.py real_estate test_docs/paris_office
"""

import argparse
import logging
import sys
from pathlib import Path
from uuid import uuid4

from dotenv import load_dotenv
load_dotenv()

from langgraph.types import Command as LGCommand

from graph.dd_graph import build_dd_graph
from graph.logging_config import setup_logging
from graph.output_writer import init_output, write_stage, finalize_output
from graph.state import DDState
from graph.stages import get_stages, DEAL_TYPE_ALIASES

log = logging.getLogger(__name__)

# ─── ANSI colours ─────────────────────────────────────────────────────────────

RESET  = "\033[0m"
BOLD   = "\033[1m"
GREEN  = "\033[32m"
RED    = "\033[31m"
YELLOW = "\033[33m"
CYAN   = "\033[36m"
DIM    = "\033[2m"


def _colour(text: str, code: str) -> str:
    return f"{code}{text}{RESET}"


def _separator(char: str = "═", width: int = 72) -> str:
    return char * width


def _print_header(deal_type: str, docs_path: str, total_stages: int) -> None:
    print()
    print(_colour(_separator(), CYAN))
    print(_colour(f"  DUE DILIGENCE ENGINE — {deal_type.upper()}", BOLD + CYAN))
    print(_colour(f"  Documents: {docs_path}", DIM))
    print(_colour(f"  Stages: {total_stages}", DIM))
    print(_colour(_separator(), CYAN))
    print()


def _print_stage_banner(stage_result: dict) -> None:
    """Print stage name + LLM suggested gate after run_stage completes."""
    name     = stage_result["name"]
    llm_gate = stage_result["gate_decision"]
    colour   = GREEN if llm_gate == "GO" else RED
    print(_colour(_separator("─"), CYAN))
    print(_colour(f"  {name}", BOLD))
    print(f"  LLM suggested gate: {_colour(llm_gate, BOLD + colour)}")
    print()


def _prompt_human_gate(interrupt_val: dict) -> str:
    """
    Block until the user types GO or NO_GO.
    Returns "GO" or "NO_GO".
    """
    stage_name = interrupt_val.get("stage_name", "?")
    llm_gate   = interrupt_val.get("llm_gate", "GO")
    stage_num  = interrupt_val.get("stage", "?")
    total      = interrupt_val.get("total", "?")

    llm_colour = GREEN if llm_gate == "GO" else RED

    print(_colour(_separator("═"), YELLOW))
    print(_colour(f"  ⚡ HUMAN GATE  —  {stage_name}", BOLD + YELLOW))
    print(_colour(f"  Stage {stage_num}/{total}", DIM))
    print(_colour(_separator("═"), YELLOW))
    print(f"  LLM recommendation: {_colour(llm_gate, BOLD + llm_colour)}")
    print()

    while True:
        raw = input(
            _colour("  Your decision → [G] GO  |  [N] NO_GO : ", BOLD + YELLOW)
        ).strip().upper()
        if raw in ("G", "GO", ""):
            print(_colour("  ✅  GO — advancing to next stage.\n", GREEN))
            return "GO"
        if raw in ("N", "NO", "NO_GO", "NOGO"):
            print(_colour("  ⛔  NO_GO — deal killed.\n", RED))
            return "NO_GO"
        print(_colour("  Invalid. Enter G (go) or N (no_go).", RED))


def _print_summary(stage_results: list[dict], final_status: str) -> None:
    print()
    print(_colour(_separator(), BOLD))
    print(_colour("  FINAL SUMMARY", BOLD + CYAN))
    print(_colour(_separator(), BOLD))
    print()

    for r in stage_results:
        gate   = r["gate_decision"]
        colour = GREEN if gate == "GO" else RED
        marker = "✓" if gate == "GO" else "✗"
        print(f"  {_colour(marker, colour)}  {r['name']}  [{_colour(gate, colour)}]")

    print()
    if final_status == "completed":
        print(_colour("  VERDICT: All gates passed — deal advanced to IC.", BOLD + GREEN))
    elif final_status == "killed":
        killed = next((r for r in reversed(stage_results) if r["gate_decision"] == "NO_GO"), None)
        label  = killed["name"] if killed else "unknown stage"
        print(_colour(f"  VERDICT: Deal killed at  {label}", BOLD + RED))
    print()
    print(_colour(_separator(), BOLD))
    print()


# ─── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    setup_logging()

    parser = argparse.ArgumentParser(
        description="Gated Due Diligence CLI powered by LangGraph + Google Gemini"
    )
    parser.add_argument(
        "deal_type",
        help=(
            "Deal type to analyse. Options: biotech, mature_mbo, real_estate. "
            f"Aliases: {list(DEAL_TYPE_ALIASES.keys())}"
        ),
    )
    parser.add_argument(
        "docs_path",
        help="Path to directory containing .txt documents for this deal",
    )
    args = parser.parse_args()

    deal_type = args.deal_type
    docs_path = args.docs_path

    if not Path(docs_path).exists():
        print(_colour(f"ERROR: docs_path '{docs_path}' does not exist.", BOLD + RED))
        sys.exit(1)

    try:
        stages = get_stages(deal_type)
    except ValueError as e:
        print(_colour(f"ERROR: {e}", BOLD + RED))
        sys.exit(1)

    log.info("Deal type  : %s", deal_type)
    log.info("Docs path  : %s", docs_path)
    log.info("Stages     : %d", len(stages))

    _print_header(deal_type, docs_path, len(stages))

    output_file = init_output(deal_type, docs_path)
    log.info("Output     : %s", output_file)

    initial_state: DDState = {
        "deal_type":           deal_type,
        "docs_path":           docs_path,
        "raw_docs":            [],
        "embeddings_path":     "",
        "stage_results":       [],
        "current_stage":       0,
        "gate_decision":       "",
        "final_status":        "in_progress",
        "total_input_tokens":  0,
        "total_output_tokens": 0,
    }

    graph  = build_dd_graph()
    config = {"configurable": {"thread_id": str(uuid4())}}

    # ── Streaming loop with HITL ──────────────────────────────────────────────
    # Each pass of the while-loop is one graph.stream() call.
    # When an interrupt fires the stream ends; we prompt the user then resume.
    stage_results_seen: list[dict] = []
    final_status  = "in_progress"
    stream_input  = initial_state   # first call uses initial_state, resumes use Command
    total_in  = 0
    total_out = 0

    while True:
        hit_interrupt      = False
        interrupt_payload  = None
        pending_result     = None   # run_stage result waiting for human gate

        for update in graph.stream(stream_input, config, stream_mode="updates"):
            for node_name, state_update in update.items():

                if node_name == "load_docs":
                    doc_count = len(state_update.get("raw_docs", []))
                    print(_colour(f"  ✓ Loaded {doc_count} document(s)\n", GREEN))

                elif node_name == "embed_docs":
                    embed_path = state_update.get("embeddings_path", "")
                    print(_colour(f"  ✓ Vector store ready — {embed_path}\n", GREEN))

                elif node_name == "run_stage":
                    new_results = state_update.get("stage_results", [])
                    total_in  += state_update.get("total_input_tokens",  0)
                    total_out += state_update.get("total_output_tokens", 0)
                    for result in new_results:
                        stage_results_seen.append(result)
                        pending_result = result
                        _print_stage_banner(result)

                elif node_name == "human_gate":
                    # Fires on RESUME — carries the final gate + final_status
                    gate        = state_update.get("gate_decision", "")
                    new_status  = state_update.get("final_status", "")
                    if new_status:
                        final_status = new_status
                    # Keep stage_results in sync with human's override
                    if stage_results_seen and gate:
                        stage_results_seen[-1]["gate_decision"] = gate

                elif node_name == "__interrupt__":
                    hit_interrupt     = True
                    interrupt_payload = state_update[0]   # Interrupt object

        if hit_interrupt:
            # Prompt for human decision
            decision = _prompt_human_gate(interrupt_payload.value)

            # Persist stage output + human gate to JSON immediately
            if pending_result:
                write_stage(output_file, pending_result, decision)

            # Feed decision back into the graph
            stream_input = LGCommand(resume=decision)

        else:
            # Graph ran to completion without an interrupt — done
            break

    finalize_output(output_file, final_status)
    _print_summary(stage_results_seen, final_status)

    print(_colour(f"  Tokens used  →  input={total_in}  output={total_out}  total={total_in+total_out}", DIM))
    print(_colour(f"  Output saved →  {output_file}", DIM))


if __name__ == "__main__":
    main()
