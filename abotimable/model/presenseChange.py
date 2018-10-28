"""
Dataclass to represent a presence change json
"""
from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class PresenseChange:
    type: str
    user: str
    presense: str
