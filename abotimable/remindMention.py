"""
    File: remindMention.py
    Version: 1.0.0
    Author: Chris Baudouin, Jr.

    Description: Reminds the recipient of a mention that they've been mentioned.
"""
from .teamBotModule import TeamBotModule
from .model.message import Message
from slackclient import SlackClient
import re
import logging
import time

logger = logging.getLogger(__name__)


class RemindMention:

    def __init__(self):
        pass

    def check_for_mention(self, message: str) -> bool:
        return "@" in message

    def process_payload(self, slack_client: SlackClient,
            message: Message) -> None:
        at_users = re.findall(r'@[a-zA-Z0-9]*', message.text)
        for at_user in at_users:
            user = at_user.lstrip('@')
            create_dm_request = slack_client.api_call(
                "conversations.open",
                users=[user]
            )
            if create_dm_request['ok'] == True:
                dm_channel_id = create_dm_request['channel']['id']
                for i in range(0, 10, 1):
                    send_dm_message = slack_client.api_call(
                        "chat.postMessage",
                        channel=dm_channel_id,
                        text="Hey! <@{}> sent you a message!".format(message.user)
                    )
                    time.sleep(2)
                logger.info("Created DM to user '{}'".format(user))
            else:
                logger.error("Error creating a DM request to slack")
                logger.error(create_dm_request)


    def notify_message(self, slack_client: SlackClient, message: Message) -> None:
        if self.check_for_mention(message.text):
            self.process_payload(slack_client, message)


TeamBotModule.register(RemindMention)
