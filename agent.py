from langgraph.graph import StateGraph
from langchain_core.messages import HumanMessage
from state import InteractionState
from llm import llm
from tools import (
    log_interaction,
    fetch_hcp_profile,
    suggest_next_best_action,
    compliance_check
)
from prompts import EXTRACTION_PROMPT
import json

def agent_node(state: InteractionState, message: str) -> InteractionState:
    response = llm.invoke([
        HumanMessage(content=EXTRACTION_PROMPT),
        HumanMessage(content=message)
    ])

    extracted = json.loads(response.content)

    if any(getattr(state, k) for k in extracted.keys()):
        return edit_interaction(state, extracted)
    else:
        return log_interaction(state, extracted)


graph = StateGraph(InteractionState)
graph.add_node("agent", agent_node)
graph.set_entry_point("agent")
graph.set_finish_point("agent")

interaction_graph = graph.compile()
