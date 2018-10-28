"""
A class to represent a simple server message
"""
from dataclasses import dataclass
from dataclasses_json import dataclass_json

@dataclass_json
@dataclass
class Message:
    type: str
    channel: str # The channel the message is in
    user: str # The UID of who made the message
    text: str # The plaintext of the message
    ts: str # The unique timestamp of the message

