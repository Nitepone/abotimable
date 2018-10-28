"""
    File: ricFlair.py
    Version: 1.0.0
    Author: Chris Baudouin, Jr.

    Description: Anytime "woo" is mentioned in chat, abotimable will post a ric flair picture
"""
import re
from .teamBotModule import TeamBotModule


class RicFlair():

    def __init__(self):
        pass

    def check_for_woo(self, message):
        match_obj = re.match(r'wo{2,} *', message)

        if match_obj:
            return
        else:
            return

    def notify_message(self, slack_client, message):
        self.check_for_woo(message)


TeamBotModule.register(RicFlair)
