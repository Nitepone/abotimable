"""
A dataclass to represent a reaction
"""
from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Reaction:
    type: str
    user: str # The UID of the user making the reaction
    reaction: str # The reaction by its string name
    item_user: str # The ID of the user being reacted to
    item: Message # The message that is being reacted to
    # Take note, the above line could be a file, and not a message
    event_ts: str # The time the reaction was made
