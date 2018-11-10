"""
    File: ricFlair.py
    Version: 1.0.0
    Author: Chris Baudouin, Jr.

    Description: Anytime "woo" is mentioned in chat, abotimable will post a ric flair picture
"""
import random
import re
from .teamBotModule import TeamBotModule

# Credit to the image owners
rics = ["https://i.pinimg.com/236x/63/47/83/634783c510e2564240db54ee141213e3--fighting-memes-ric-flair.jpg",
        "https://img.buzzfeed.com/buzzfeed-static/static/2015-03/13/16/enhanced/webdr10/enhanced-buzz-1212-1426277573-14.jpg",
        "https://i.ytimg.com/vi/XB21XNxtk5M/hqdefault.jpg"]


class RicFlair():

    def __init__(self):
        pass

    def check_for_woo(self, slack_client, message):
        match_obj = re.match(r'wo{2,} *', message.text)
        if match_obj:
            rand = random.randint(0, len(rics)-1)
            message_response = slack_client.api_call(
                "chat.postMessage",
                channel=message.channel,
                attachments=[{"fallback": "Required plain-text summary of the attachment.",
                              "image_url": rics[rand]}])

    def notify_message(self, slack_client, message):
        self.check_for_woo(slack_client, message)


TeamBotModule.register(RicFlair)
