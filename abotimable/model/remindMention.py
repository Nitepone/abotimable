"""
    File: remindMention.py
    Version: 1.0.0
    Author: Chris Baudouin, Jr.

    Description: Reminds the recipient of a mention that they've been mentioned.
"""
from ..teamBotModule import TeamBotModule


class RemindMention():

    def __init__(self):
        pass

    def check_for_mention(message):
        if "@" in message:
            return True
        else:
            return False

    def process_payload(payload):
        return

    def notify_message(self, team_rtm, message):
        pass


TeamBotModule.register(RemindMention)
