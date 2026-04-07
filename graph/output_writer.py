"""
Incremental JSON output writer.

Writes to: assets_output/<deal_type>_<folder_name>.json
Updated after every stage so partial results survive an early kill.
"""

import json
import logging
from datetime import datetime
from pathlib import Path

log = logging.getLogger(__name__)

OUTPUT_BASE = Path("assets_output")


def output_path(deal_type: str, docs_path: str) -> Path:
    folder_name = Path(docs_path).name          # e.g. "paris_office"
    filename    = f"{deal_type}_{folder_name}.json"
    return OUTPUT_BASE / filename


def init_output(deal_type: str, docs_path: str) -> Path:
    OUTPUT_BASE.mkdir(exist_ok=True)
    path = output_path(deal_type, docs_path)
    data = {
        "deal_type":          deal_type,
        "docs_path":          docs_path,
        "run_date":           datetime.now().isoformat(timespec="seconds"),
        "stages":             {},
        "final_status":       "in_progress",
        "total_input_tokens":  0,
        "total_output_tokens": 0,
    }
    path.write_text(json.dumps(data, indent=2))
    log.info("Output file initialised → %s", path)
    return path


def write_stage(path: Path, stage_result: dict, human_gate: str) -> None:
    data       = json.loads(path.read_text())
    stage_name = stage_result["name"]

    in_tok  = stage_result.get("input_tokens", 0)
    out_tok = stage_result.get("output_tokens", 0)

    data["stages"][stage_name] = {
        "stage_index":    stage_result["stage"],
        "output":         stage_result["output"],   # structured JSON dict
        "llm_gate":       stage_result["gate_decision"],
        "human_gate":     human_gate,
        "input_tokens":   in_tok,
        "output_tokens":  out_tok,
        "total_tokens":   in_tok + out_tok,
    }

    data["total_input_tokens"]  = data.get("total_input_tokens", 0)  + in_tok
    data["total_output_tokens"] = data.get("total_output_tokens", 0) + out_tok

    path.write_text(json.dumps(data, indent=2))
    log.info(
        "Stage saved  %-40s  human=%s  tokens in=%d out=%d",
        stage_name, human_gate, in_tok, out_tok,
    )


def finalize_output(path: Path, final_status: str) -> None:
    data = json.loads(path.read_text())
    data["final_status"] = final_status
    total_in  = data.get("total_input_tokens", 0)
    total_out = data.get("total_output_tokens", 0)
    path.write_text(json.dumps(data, indent=2))
    log.info(
        "Output finalised → %s  status=%s  total tokens in=%d out=%d",
        path, final_status, total_in, total_out,
    )
