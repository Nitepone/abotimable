"""
    File: remindMention.py
    Version: 1.0.0
    Author: Chris Baudouin, Jr.

    Description: Reminds the recipient of a mention that they've been mentioned.
"""
from ..teamBotModule import TeamBotModule
import re


class RemindMention():

    def __init__(self):
        pass

    def check_for_mention(self, message):
        if "@" in message:
            return True
        else:
            return False

    def process_payload(self, slack_client, message):
        nonsplit_user = re.findall(r'@.[a-z]*', message)
        user = re.split('@', nonsplit_user[0])[1]
        create_dm_request = slack_client.api_call(
            "conversations.open",
            users=[user]
        )
        if create_dm_request['ok'] == True:
            dm_channel_id = create_dm_request['channel']['id']
            send_dm_message = slack_client.api_call(
                "chat.postMessage",
                channel = dm_channel_id,
                text = "Hey! " + nonsplit_user[0] + " sent you a message!"
            )


    def notify_message(self, slack_client, message):
        if self.check_for_mention(message):
            self.process_payload(slack_client, message)


TeamBotModule.register(RemindMention)
