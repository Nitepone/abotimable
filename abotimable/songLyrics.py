"""
FILE: songLyrics.py
PROJECT: abotimable

Sometimes you're chatting with your buds and
you get into an argument about the words to
"Africa" by Toto. In these cases, it's super handy
to have a tool that can look up the lyrics for
you. This is almost what this module does.

Abotimable tries. He really does. But sometimes
he mishears the name of the artist/band/song.
Mistakes happen. Don't worry about it.

@author Trevor S. (txs6996)
@version 1.0.2

"""
import logging
import random
import configparser
import lyricsgenius as genius
from slackclient import SlackClient
from .model.message import Message

logger = logging.getLogger(__name__)

config = configparser.RawConfigParser()
config.read('config.ini')

client_id = config['GENIUS']['CLIENT_ACCESS_TOKEN']
api = genius.Genius(client_id)

smart_responses = ["one sec, let me see if i can remember that one",
                   "please don't start singing",
                   "please stop asking me to look up this junk",
                   "lol people still listen to that?"]


def buildmessage(channel, text):
    msg = {
        channel: channel,
        text: text
    }


def song_lookup(song, artist, slack_client, message):
    rand = random.randint(0, 1)
    rand_msg = random.randint(0, len(smart_responses)-1)  # Choose a random smart response

    message_response = slack_client.api_call(
        "chat.postMessage",
        channel=message.channel,
        text=("<@{}> " + smart_responses[rand_msg]).format(message.user)
    )

    if rand == 0:
        # Get the wrong artist
        s = api.search_song(song)
        return s

    else:
        # Get the wrong song name
        max_songs = 5  # Max number of songs to search for on Artist profile
        a = api.search_artist(artist, max_songs)
        s = a.songs[random.randint(0, max_songs-1)]
        while s.title == song:
            s = a.songs[random.randint(0, max_songs-1)]
        return s


class SongLyricsModule:

    def notify_message(self, slack_client: SlackClient, message: Message) -> None:
        try:
            if "!lyrics" in message.text.lower():
                song, artist = message.text.lstrip('!lyrics').split(',')
                song = song_lookup(song, artist, slack_client, message)
                message_response = slack_client.api_call(
                    "chat.postMessage",
                    channel=message.channel,
                    text=song
                )
        except Exception:
            pass


if __name__ == '__main__':
    incoming = ""
    song = song_lookup("Coheed and Cambria", "Garbage")
