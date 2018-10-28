"""
Test module that simply prints recieved notifications
"""

from .teamBotModule import TeamBotModule


class TestModule:

    def __init__(self):
        pass

    def notify_message(self, slack_client, message):
        print(message.text)


TeamBotModule.register(TestModule)
