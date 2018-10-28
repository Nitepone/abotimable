"""
    File: remindMention.py
    Version: 1.0.0
    Author: Chris Baudouin, Jr.

    Description: Reminds the recipient of a mention that they've been mentioned.
"""
from ..teamBotModule import TeamBotModule

class remindMention():

    def __init__(self):
        pass

    def check_for_mention(message):
        if "@" in message:
            return True
        else:
            return False


    def process_payload(payload):
        return

    def notifyMessage(self, teamRTM, message):
        pass

TeamBotModule.register(remindMention)