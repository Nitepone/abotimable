import time
import logging
import coloredlogs
import json
from slackclient import SlackClient
from abotimable.model import bot as bot_model
from abotimable.model.message import Message
from abotimable.model.reaction import Reaction
from abotimable.testmodule import TestModule
from abotimable.remindMention import RemindMention
from abotimable.grammar import GrammarModule
from abotimable.emotionmodule import EmotionModule
from abotimable.superiorOS import SuperiorOSModule

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
    SuperiorOSModule()
]

def main():
    for bot in bot_model.get_bots():
        sc = SlackClient(bot.bot_access_token)

        # notify general that the bot is online
        sc.api_call(
          "chat.postMessage",
          channel="general",
          text="Your favorite bot is back online. :tada:"
        )

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
                        observer.notify_message(sc, item)

                time.sleep(1)
        else:
            logger.error("Connection Failed")

if __name__ == "__main__":
    main()
