from langchain.tools import tool
from state import InteractionState

@tool
def log_interaction(state: InteractionState, extracted_data: dict) -> InteractionState:
    """
    Logs a new interaction by populating empty fields.
    """
    for key, value in extracted_data.items():
        if getattr(state, key) in [None, [], ""]:
            setattr(state, key, value)
    return state

def edit_interaction(state: InteractionState, updates: dict) -> InteractionState:
    """
    Updates existing interaction fields based on user correction.
    """
    for key, value in updates.items():
        setattr(state, key, value)
    return state

def fetch_hcp_profile(hcp_name: str) -> dict:
    """
    Fetches historical context for the HCP (mocked).
    """
    return {
        "hcp_name": hcp_name,
        "specialty": "Cardiology",
        "previous_interactions": 5
    }

def suggest_next_best_action(state: InteractionState) -> str:
    """
    Suggests follow-up actions based on interaction.
    """
    if "drug" in " ".join(state.topics).lower():
        return "Schedule follow-up visit and share clinical material."
    return "No immediate action suggested."

def compliance_check(summary: str) -> bool:
    """
    Basic compliance validation.
    """
    restricted_terms = ["guaranteed", "cure"]
    return not any(term in summary.lower() for term in restricted_terms)
