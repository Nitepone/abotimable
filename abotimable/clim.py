"""
    File: clim.py
    Version: 1.0.1
    Author: Chris Baudouin, Jr.

    Description: All clim-related features including but not limited to: "you
                 got clim'd!", climtistics and more.
"""
from .teamBotModule import TeamBotModule
from .model.message import Message
from slackclient import SlackClient
import logging
import re

logger = logging.getLogger(__name__)


class Clim:

    def __init__(self):
        pass

    def its_clim(self, message: Message) -> bool:
        if "@" in message.text and message.user == "U2AEM0BSA":
            return True
        else:
            return False

    def clim_em(self, slack_client, message):
        recipients = re.findall(r'@[a-zA-Z0-9]*', message.text)
        for recipient in recipients:
            message_response = slack_client.api_call(
                "chat.postMessage",
                channel=message.channel,
                text="_<@{}> you just got clim'd!_"
                     .format(str(recipient).strip("@"))
            )

    def notify_message(self, slack_client: SlackClient,
                       message: Message) -> None:
        if self.its_clim(message):
            self.clim_em(slack_client, message)


TeamBotModule.register(Clim)
