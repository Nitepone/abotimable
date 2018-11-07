"""
FILE: greeter.py
PROJECT: abotimable

Your friendly neighborhood abotimable just wants
to check in and make sure everyone is having a fun
and productive time. That's why he wakes up every
6-24 hours and just says hello. Gotta keep that
team morale up!

@author Trevor S. (txs6996)
@version 1.0.1

"""
import logging
import random
import time
from slackclient import SlackClient
from .teamBotModule import TeamBotModule
from .model.message import Message

logger = logging.getLogger(__name__)

greeting = "Hello everybody! Hope <!everyone> is having a wonderful and productive day :)"


class GreeterModule:

    def __init__(self):
        self.running = False


    def run_greeter(self, sc: SlackClient, channel):
        if self.running:
            return
        else:
            self.running = True
            logger.info("Greeter sleeping for 50 seconds")
            time.sleep(50)      # wait slightly for first message
            while self.running:
                sc.api_call("chat.postMessage", channel=channel, text=greeting)
                numhours = random.randint(6, 24)
                sleeptime = numhours * 3600
                logger.info("Greeter sleeping for {} seconds".format(sleeptime))
                time.sleep(sleeptime)


    def notify_message(self, slack_client: SlackClient, message: Message) -> None:
        self.run_greeter(slack_client, message.channel)

TeamBotModule.register(GreeterModule)
