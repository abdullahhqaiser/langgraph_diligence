import operator
from typing import Annotated
from typing_extensions import TypedDict


class DDState(TypedDict):
    deal_type: str
    docs_path: str
    raw_docs: list[str]
    embeddings_path: str          # path to persisted Chroma store
    stage_results: Annotated[list[dict], operator.add]
    current_stage: int
    gate_decision: str            # "GO" | "NO_GO" | ""
    final_status: str             # "in_progress" | "completed" | "killed"
    total_input_tokens: Annotated[int, operator.add]
    total_output_tokens: Annotated[int, operator.add]
