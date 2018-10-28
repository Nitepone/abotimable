"""
Test module that simply prints recieved notifications
"""

from .teamBotModule import TeamBotModule

class TestModule:

    def __init__(self):
        pass

    def notifyMessage(self, teamRTM, message):
        print(message.text)

TeamBotModule.register(TestModule)
