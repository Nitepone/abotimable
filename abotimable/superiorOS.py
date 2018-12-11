"""
FILE: superiorOS.py
PROJECT: abotimable

Everyone knows that GapDash is the best operating system
available. Still, it's so much fun to incite wars, isn't
it? This module will listen for people to mention Windows
or macOS (or iOS), and tell people that whatever they've
said is wrong. Built to be argumentative, whether the
inciting comment was for or against the OS in question.

Linux is completely ignored in this module. Because
why would anyone say anything about Linux?

@author Trevor S. (txs6996)
@version 1.0.1

"""
import logging
import random
from slackclient import SlackClient
from .teamBotModule import TeamBotModule
from .model.message import Message

logger = logging.getLogger(__name__)


def buildmessage(channel, text):
    msg = {
        channel: channel,
        text: text
    }


def contains_os_mention(text):
    contents = ""
    if "windows" in text.lower():
        contents += "windows"
    elif "macos" in text.lower() or "osx" in text.lower():
        contents += "mac"
    elif "android" in text.lower():
        contents += "android"
    elif "iphone" in text.lower() or "apple" in text.lower():
        contents += "iphone"

    if "good" in text.lower() or "best" in text.lower() \
            or "better" in text.lower():
        contents += "-pos"
    if "bad" in text.lower() or "worst" in text.lower() \
            or "worse" in text.lower() or "shit" in text.lower():
        contents += "-neg"

    return contents


def prepare_counterargument(classification):
    counter = ""
    if classification == "windows-pos":
        counter = "At least my computer updates without committing seppuku."
    elif classification == "windows-neg":
        counter = "Windows machines are scientifically proven to be superior."
    elif classification == "mac-pos":
        counter = "Mehhhhhhhhhhhh. Apple sucks!"
    elif classification == "mac-neg":
        counter = "Steve Jobs was a god."
    elif classification == "android-pos":
        counter = "Fuckin' greenie"
    elif classification == "android-neg":
        counter = "Yeah? How's your screen doing?"
    elif classification == "iphone-pos":
        counter = "overpriced garbage lol"
    elif classification == "iphone-neg":
        counter = "But all of my preferences are synced across everything ever."

    return counter


class SuperiorOSModule:

    def notify_message(self, slack_client: SlackClient, message: Message) -> None:
        incoming = message.text
        hot_contents = contains_os_mention(incoming)
        rand = random.randint(1, 10)
        if hot_contents != "":
            outgoing = prepare_counterargument(hot_contents)
            message_response = slack_client.api_call(
                "chat.postMessage",
                channel = message.channel,
                text = outgoing
            )
            logger.debug("Sent: {}".format(outgoing))
        else:
            logger.debug("No hot contents found for OS")


TeamBotModule.register(SuperiorOSModule)


if __name__ == '__main__':
    incoming = "iphones are so much better"
    hot_contents = contains_os_mention(incoming)
    print(incoming)
    rand = random.randint(1, 10)
    if hot_contents != "":
        outgoing = prepare_counterargument(hot_contents)
        print(outgoing)
