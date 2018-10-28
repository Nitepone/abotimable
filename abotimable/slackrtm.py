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

coloredlogs.install(level=logging.DEBUG)
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
    SongLyricsModule()
]

def bot_loop(bot: bot_model.Bot) -> None:
    sc = SlackClient(bot.bot_access_token)

    # here's where we do the stuff
    if sc.rtm_connect(with_team_state=False):
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
                for observer in team_bot_modules:
                    t = threading.Thread(
                        target=observer.notify_message,
                        args=(sc, item),
                        daemon=True
                    )
                    t.start()

            time.sleep(1)
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

def main():
    threads = []

    for bot in bot_model.get_bots():
        t = threading.Thread(target=bot_loop_monitor, args=(bot,))
        t.start()
        threads.append(t)

if __name__ == "__main__":
    main()
