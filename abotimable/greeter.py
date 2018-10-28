"""
FILE: greeter.py
PROJECT: abotimable

Your friendly neighborhood abotimable just wants
to check in and make sure everyone is having a fun
and productive time. That's why he wakes up every
6-24 hours and just says hello. Gotta keep that
team morale up!

@author Trevor S. (txs6996)
@version 1.0

"""

from slackclient import SlackClient
from .model.message import Message
import time
import random


greeting = "Hello everybody! Hope <@everyone> is having a wonderful and productive day :)"


def __init__(self):
    self.running = False


def run_greeter(self, sc: SlackClient, channel):
    if self.running:
        return
    else:
        self.running = True
        time.sleep(50)      # wait slightly for first message
        while self.running:
            sc.api_call("chat.postMessage", channel=channel, text=greeting)
            numhours = random.randint(6, 24)
            sleeptime = numhours * 3600
            time.sleep(sleeptime)


def notify_message(self, slack_client: SlackClient, message: Message) -> None:
    run_greeter(self, slack_client, message.channel)
