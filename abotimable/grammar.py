"""
FILE: grammar.py
PROJECT: abotimable

In an effort to make a very annoying slack bot, why not
start with a module that corrects your improper grammar,
you heathen? Hey, maybe sometimes he makes mistakes, but
don't worry about it. He's making the world a better place.

@author Trevor S. (txs6996)
@version 1.0

"""
import logging
import random
from slackclient import SlackClient
from .teamBotModule import TeamBotModule
from .model.message import Message
from .settings import Settings

logger = logging.getLogger(__name__)

settings = Settings()

grammar_errors = {
    "you're": "your",
    "your": "you're",
    "their": "there",
    "they're": "their",
    "there": "they're",
    "who": "whom",
    "whom": "who",
    "its": "it's",
    "it's": "its",
    "while": "whilst",
    "whilst": "while"
}


def buildmessage(channel, text):
    msg = {
        channel: channel,
        text: text
    }


def containscommonissue(text):
    for word in grammar_errors:
        if word in text.lower():
            return word
    return None


def correctgrammar(word):
    corrected = grammar_errors[word.lower()]
    return "Just a heads up, " + word + \
           " should actually be " + corrected


class GrammarModule:

    def notify_message(self, slack_client: SlackClient,
            message: Message) -> None:
        incoming = message.text
        word = containscommonissue(incoming)
        rand = random.random()
        if word is not None and rand < settings.annoyance:
            outgoing = correctgrammar(word)
            message_response = slack_client.api_call(
                "chat.postMessage",
                channel = message.channel,
                text = outgoing
            )
            logger.debug("Grammar module sent message: {}".format(outgoing))
            logger.debug("Reponse: {}".format(message_response))
        else:
            logger.debug("Grammar module is skipping post")

TeamBotModule.register(GrammarModule)

if __name__ == '__main__':
    incoming = "Hey man, you're gonna be late!"
    word = containscommonissue(incoming)
    print(incoming)
    rand = random.randint(1, 20)
    if word is not None and rand <= 3:
        outgoing = correctgrammar(word)
        print(outgoing)
