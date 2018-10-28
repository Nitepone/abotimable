import time, logging, json
from slackclient import SlackClient
from abotimable.model import bot as BotModel
from abotimable.model.message import Message
from abotimable.model.reaction import Reaction
from abotimable.testmodule import TestModule

logging.basicConfig(level=logging.DEBUG)

item_types = {
    "message": Message,
    "reaction": Reaction,
}

team_bot_modules = [
    TestModule()
]

for bot in BotModel.get_bots():
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
                logging.debug(item_dict)
                assert isinstance(item_dict, dict)

                item_type = item_dict["type"]
                if item_type not in item_types:
                    continue
                item = item_types[item_type].from_json(json.dumps(item_dict))
                for observer in team_bot_modules:
                    observer.notifyMessage(sc, item)

            time.sleep(1)
    else:
        logging.error("Connection Failed")
