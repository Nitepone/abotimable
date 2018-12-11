import pickle
import shelve
import time
import logging
import coloredlogs
import json
import threading
from slackclient import SlackClient
from abotimable.model import bot as bot_model
from abotimable.model.message import Message
from abotimable.model.reaction import Reaction
from abotimable.testmodule import TestModule
from abotimable.remindMention import RemindMention
from abotimable.grammar import GrammarModule
from abotimable.emotionmodule import EmotionModule
from abotimable.superiorOS import SuperiorOSModule
from abotimable.greeter import GreeterModule
from abotimable.lmgtfy import LMGTFYModule
from abotimable.songLyrics import SongLyricsModule
from abotimable.clim import Clim
from abotimable.ricFlair import RicFlair

coloredlogs.install(level=logging.BASIC_FORMAT)
logger = logging.getLogger(__name__)

item_types = {
    "message": Message,
    "reaction": Reaction,
}

team_bot_modules = [
    TestModule(),
    RemindMention(),
    GrammarModule(),
    EmotionModule(),
    SuperiorOSModule(),
    GreeterModule(),
    LMGTFYModule(),
    SongLyricsModule(),
    Clim(),
    RicFlair()
]


def bot_loop(bot: bot_model.Bot) -> None:
    logger.info("Starting bot loop for bot: " + bot.team_name)
    sc = SlackClient(bot.bot_access_token)

    # here's where we do the stuff
    if sc.rtm_connect(with_team_state=False):
        # check for preferences
        while True:
            item_list = sc.rtm_read()
            assert isinstance(item_list, list)

            for item_dict in item_list:
                logger.debug(item_dict)
                assert isinstance(item_dict, dict)

                item_type = item_dict["type"]
                if item_type not in item_types:
                    continue
                # skip bot messages
                if item_dict.get('subtype', None) == 'bot_message':
                    continue
                # unpack message edits
                while item_dict.get('subtype', None) == "message_changed":
                    channel = item_dict['channel']
                    item_dict = item_dict['message']
                    item_dict['channel'] = channel
                item = item_types[item_type].from_json(json.dumps(item_dict))
                time.sleep(1)  # Adds human like delay to responding
                for observer in team_bot_modules:
                    try:
                        t = threading.Thread(
                            target=observer.notify_message,
                            args=(sc, item),
                            daemon=True
                        )
                        t.start()
                    except:
                        logger.error("Error starting thread")
    else:
        logger.error("Connection Failed")


def bot_loop_monitor(bot: bot_model.Bot) -> None:
    timeout = 1
    while True:
        try:
            bot_loop(bot)
        except Exception:
            pass
        time.sleep(timeout)
        timeout = timeout * 2


def start_bot_monitor(bot: bot_model.Bot) -> None:
    threading.Thread(target=bot_loop_monitor, args=(bot,)).start()


def main():
    for bot in bot_model.get_bots():
        start_bot_monitor(bot)


if __name__ == "__main__":
    main()
