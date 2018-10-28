"""
Test module that simply prints recieved notifications
"""

from .teamBotModule import TeamBotModule
from .model.message import Message
from slackclient import SlackClient

class TestModule:

    def __init__(self):
        pass


    def notify_message(self, team_rtm: SlackClient,
            message: Message) -> None:
        print(message.text)

TeamBotModule.register(TestModule)
