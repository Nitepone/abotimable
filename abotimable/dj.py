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

ACCEPTED = 202
NOT_ACCEPTED = 406
DISABLED = 407
EXPLICIT = 405
NOT_FOUND = 404
ERROR = 500

# When Spotiserver likes the song
accepted_responses = ["i got u",
                      "i added it to the list",
                      "added to the request list!",
                      "turning up the volume for that one",
                      "got it! remember the more requests i get for a song, the more likely i am to choose it"]

# When a listener requests too many songs or the same song
not_accepted_responses = ["you need to slow down",
                               "who made you the DJ?",
                               "can't take that request, gotta slow you down",
                               "no"]

# When Spotiserver isn't taking requests
disabled_responses = ["i'm not taking requests right now",
                      "ask slackbot to play that",
                      "no"]

# Spotiserver deems that song explicit
explicit_responses = ["sorry, that's explicit",
                      "that has bad words!",
                      "this is a PG event",
                      "come on, seriously? no."]

not_found_responses = ["yo, can't find that one",
                       "don't know that, make sure you supply me with the artist too",
                       "never heard of that song"]

error_responses = ["something very serious happened internally"]

need_artist_responses = ["need the artist",
                         "!request <track>, <artist>"]


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
