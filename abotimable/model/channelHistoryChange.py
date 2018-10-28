"""
Dataclass for channel history changes
"""
from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class ChannelHistoryChange:
    type: str
    latest: str
    ts: str
    event_ts: str
