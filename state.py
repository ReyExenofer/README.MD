from typing import List, Optional
from dataclasses import dataclass, field

@dataclass
class InteractionState:
    hcp_name: Optional[str] = None
    date: Optional[str] = None
    time: Optional[str] = None
    attendees: List[str] = field(default_factory=list)
    topics: List[str] = field(default_factory=list)
    summary: Optional[str] = None
