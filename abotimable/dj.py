"""
Integration with chrisbaudouinjr/spotiserver
"""
import logging
import random
from .model.message import Message
from slackclient import SlackClient
import requests
import configparser

logger = logging.getLogger(__name__)

# When Spotiserver likes the song
accepted_responses = ["i got u",
                      "i added it to the list",
                      "added to the request list!",
                      "turning up the volume for that one",
                      "got it! remember the more requests i get for a song, the more likely i am to choose it"]


class Spotify:

    def __init__(self):
        config = configparser.RawConfigParser()
        config.read('config.ini')
        self.url = config['DJ']['URL']
        logger.info("DJ module instantiated")

    def process_request(self, slack_client: SlackClient, message: Message):
        bang, args = message.text.split(maxsplit=1)
        assert "!request" == bang.strip()
        pieces = list(map(lambda x: x.strip(), args.split(',')))
        if len(pieces) == 2:
            song, artist = pieces
            payload = {'track': song, 'artist': artist, 'listener': message.user}
            r = requests.get(self.url, params=payload)
            logger.info("Sent request to {}".format(r.url))

            if r.status_code == 200:
                j = r.json()
                self.sendMessage(slack_client, message, accepted_responses)
            else:
                try:
                    j = r.json()
                    self.sendMessage(slack_client, message, [j["message"]])
                except Exception:
                    self.sendMessage(slack_client, message, ["I can't help you right now.", "Try again later"])

    def sendMessage(self, slack_client: SlackClient, message: Message, responseList):
        rand_msg = random.randint(0, len(responseList) - 1)  # Choose a random message from response list

        message_response = slack_client.api_call(
            "chat.postMessage",
            channel=message.channel,
            text=("<@{}> " + responseList[rand_msg]).format(message.user),
            thread_ts=message.ts
        )

    def notify_message(self, slack_client: SlackClient, message: Message) -> None:
        # IMPORTANT: This feature is currently supported by only one Slack workspace
        if "!request" in message.text:
            self.process_request(slack_client, message)
