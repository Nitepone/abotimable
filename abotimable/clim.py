"""
    File: clim.py
    Version: 1.0.0
    Author: Chris Baudouin, Jr.

    Description: All clim-related features including but not limited to: "you got clim'd!", climtistics and more.
"""
from .teamBotModule import TeamBotModule
from .model.message import Message
from slackclient import SlackClient
import logging

logger = logging.getLogger(__name__)


class Clim:

    def __init__(self):
        pass

    def notify_message(self, slack_client: SlackClient, message: Message) -> None:
        pass


TeamBotModule.register(Clim)
