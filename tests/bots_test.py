"""
Test creation and query of bots from database

.. note:: must be run on a new database
    consider running `rm sqlite3.db` before running this
"""
import logging
from abotimable.model import bot as BotModel

logging.basicConfig(level=logging.DEBUG)

# create a new bot
logging.info("Creating a new bot")
b = BotModel.Bot(team_name="abcde", team_id="teamid", token="mytoken")
b.save()

# ensure that the bot is in the database
logging.info("Checking for bot in database")
try:
    next(filter(lambda b: b.team_name == "abcde", BotModel.get_bots()))
    logging.info("Found bot successfully")
except sqlite3.OperationalError as e:
    logging.error(e)