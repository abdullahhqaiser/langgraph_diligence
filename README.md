# LangGraph Due Diligence Engine

An AI-powered, gated due diligence CLI built with **LangGraph**, **Google Gemini**, and **ChromaDB**. It systematically analyses investment datarooms through structured multi-stage workflows, with a human-in-the-loop gate between each stage.

---

## Overview

The engine reads a folder of deal documents, embeds them into a persistent vector store, then runs each due diligence stage sequentially. After every stage the LLM outputs a `GO` / `NO_GO` recommendation — and a human operator confirms or overrides before the next stage begins. If any stage is killed, the run terminates early and results saved so far are preserved.

```
Documents → Embed → Stage 0 → Human Gate → Stage 1 → Human Gate → ... → Final Report
```

---

## Supported Deal Types

| Deal Type | CLI argument | Stages |
|-----------|-------------|--------|
| Biotech / Life Sciences | `biotech` | 5 (Teaser → IP & Regulatory Pre-Screen) |
| Mature MBO / Private Equity | `mature_mbo` or `mbo` | 5 (Teaser → Pre-LOI Risk Mapping) |
| Real Estate | `real_estate`, `re`, or `paris_office` | 5 (Teaser → Pre-Exclusivity Risk Mapping) |

---

## Architecture

```
main.py                    ← CLI entry point, human-gate loop
graph/
├── dd_graph.py            ← LangGraph StateGraph definition
├── state.py               ← DDState (TypedDict)
├── nodes.py               ← load_docs, embed_docs, run_stage, human_gate nodes
├── embeddings_store.py    ← ChromaDB build/load with fingerprint caching
├── loader.py              ← Raw .txt file loader
├── output_writer.py       ← Incremental JSON report writer
├── logging_config.py      ← Logging setup
└── stages/
    ├── biotech.py         ← Biotech stage definitions
    ├── mature_mbo.py      ← MBO stage definitions
    └── real_estate.py     ← Real estate stage definitions
```

### LangGraph Flow

```
START → load_docs → embed_docs → run_stage → human_gate
                                      ↑              |
                                      └── (loop) ────┘ (until all stages or NO_GO)
```

- **`load_docs`** — reads all `.txt` files from the provided folder
- **`embed_docs`** — builds or loads a persisted ChromaDB vector store (fingerprinted by folder path, never re-embedded if already cached)
- **`run_stage`** — retrieves semantically relevant chunks, calls Gemini to produce a structured JSON analysis with checklist findings, kill criteria results, summary, and gate decision
- **`human_gate`** — uses LangGraph `interrupt()` to pause execution and prompt the operator to confirm or override the LLM gate recommendation

---

## Tech Stack

| Component | Library |
|-----------|---------|
| Agent framework | `langgraph` |
| LLM | `langchain-google-genai` (Gemini 2.5 Flash) |
| Embeddings | `langchain-google-genai` (gemini-embedding-001) |
| Vector store | `langchain-chroma` (persisted ChromaDB) |
| Text splitting | `langchain-text-splitters` |
| State checkpointing | `langgraph` `InMemorySaver` |

---

## Setup

### Prerequisites

- Python 3.10+
- A Google AI API key with access to Gemini models

### Installation

```bash
# Clone the repository
git clone https://github.com/abdullahhqaiser/langgraph_diligence.git
cd langgraph_diligence

# Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate

# Install dependencies
pip install langchain langgraph langchain-google-genai langchain-chroma \
            langchain-text-splitters langchain-core python-dotenv
```

### Environment Variables

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key_here
```

---

## Usage

```bash
python main.py <deal_type> <docs_path>
```

### Examples

```bash
# Biotech deal
python main.py biotech test_docs/biotech

# Mature MBO
python main.py mature_mbo test_docs/mature_mbo

# Real estate (Paris office)
python main.py real_estate test_docs/paris_office
```

### Human Gate Interaction

After each stage completes, the engine pauses and displays the LLM's recommendation:

```
════════════════════════════════════════════════════════════════════════
  ⚡ HUMAN GATE  —  Stage 1 — Biology & Mechanism Plausibility
  Stage 1/5
════════════════════════════════════════════════════════════════════════
  LLM recommendation: GO

  Your decision → [G] GO  |  [N] NO_GO :
```

- Press `G` or `Enter` to advance
- Press `N` to kill the deal at this stage

---

## Output

Results are written incrementally to `assets_output/<deal_type>_<folder_name>.json` after every stage. The file is created at run start and updated after each gate — so partial results are never lost if a deal is killed early.

### Output Structure

```json
{
  "deal_type": "real_estate",
  "docs_path": "test_docs/paris_office",
  "run_date": "2026-04-08T03:20:00",
  "stages": {
    "Stage 0 — Teaser & Reality Check": {
      "stage_index": 0,
      "output": {
        "checklist_findings": [...],
        "kill_criteria_results": [...],
        "summary": "...",
        "gate_decision": "GO",
        "gate_reasoning": "..."
      },
      "human_gate": "GO",
      "input_tokens": 1200,
      "output_tokens": 480
    }
  },
  "final_status": "completed",
  "total_input_tokens": 8400,
  "total_output_tokens": 2100
}
```

`final_status` is one of:
- `in_progress` — run is ongoing
- `completed` — all stages passed
- `killed` — a NO_GO gate was triggered

---

## Embeddings Cache

Vector stores are persisted under `embeddings/<fingerprint>/` where the fingerprint is a short MD5 of the resolved document folder path. The same deal is never re-embedded on subsequent runs. To force a rebuild, delete the corresponding folder inside `embeddings/`.

---

## Project Structure

```
.
├── main.py                        ← CLI + human-gate event loop
├── .env                           ← API keys (not committed)
├── .gitignore
├── graph/
│   ├── dd_graph.py
│   ├── state.py
│   ├── nodes.py
│   ├── embeddings_store.py
│   ├── loader.py
│   ├── output_writer.py
│   ├── logging_config.py
│   └── stages/
│       ├── biotech.py
│       ├── mature_mbo.py
│       └── real_estate.py
├── test_docs/
│   ├── biotech/                   ← Sample Novacure biotech dataroom
│   ├── mature_mbo/                ← Sample Pinnacle MBO dataroom
│   └── paris_office/              ← Sample Paris office real estate dataroom
├── assets_output/                 ← Generated JSON reports
└── embeddings/                    ← Persisted ChromaDB vector stores
```

---

## Adding a New Deal Type

1. Create a new file `graph/stages/<deal_type>.py` and define a list of stage dicts with keys: `name`, `objective`, `checklist`, `kill_criteria`, `max_words`
2. Import and register it in `graph/stages/__init__.py` under `STAGE_REGISTRY`
3. Add any CLI aliases to `DEAL_TYPE_ALIASES`

---

## License

MIT
