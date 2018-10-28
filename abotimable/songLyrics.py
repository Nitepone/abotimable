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
@version 1.0

"""
import logging
import random
import configparser
import lyricsgenius as genius
from slackclient import SlackClient
from .teamBotModule import TeamBotModule
from .model.message import Message

logger = logging.getLogger(__name__)

config = configparser.RawConfigParser()
config.read('config.ini')

client_id = config['GENIUS']['CLIENT_ACCESS_TOKEN']
api = genius.Genius(client_id)


def buildmessage(channel, text):
    msg = {
        channel: channel,
        text: text
    }


def song_lookup(artist, song):
    rand = random.randint(0, 1)
    if rand == 0:
        # Get the wrong artist
        s = api.search_song(song)
        return s

    else:
        # Get the wrong song name
        a = api.search_artist(artist, max_songs=5)
        for s in a.songs:
            if s.title != song:
                return s

class SongLyricsModule:

    def notify_message(self, slack_client: SlackClient,
            message: Message) -> None:
        song = song_lookup("", message.text)
        message_response = slack_client.api_call(
            "chat.postMessage",
            channel = message.channel,
            text = song
        )


if __name__ == '__main__':
    incoming = ""
    song = song_lookup("Coheed and Cambria", "Garbage")
    print(song)
