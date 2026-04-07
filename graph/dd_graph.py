from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver

from graph.state import DDState
from graph.nodes import load_docs, embed_docs, run_stage, human_gate


def build_dd_graph():
    graph = (
        StateGraph(DDState)
        .add_node("load_docs", load_docs)
        .add_node("embed_docs", embed_docs)
        .add_node("run_stage", run_stage)
        .add_node("human_gate", human_gate)
        .add_edge(START, "load_docs")
        .add_edge("load_docs", "embed_docs")
        .add_edge("embed_docs", "run_stage")
        .add_edge("run_stage", "human_gate")
        # human_gate uses Command(goto=...) so no explicit edges needed for its routing
        .compile(checkpointer=InMemorySaver())
    )
    return graph
