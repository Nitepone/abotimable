"""
Test creation and query of bots from database

.. note:: must be run on a new database
    consider running `rm sqlite3.db` before running this
"""
import logging, sqlite3
from abotimable.model import bot as BotModel

logging.basicConfig(level=logging.DEBUG)

# create a new bot
logging.info("Creating a new bot")
b = BotModel.Bot(
    team_name="abcde",
    team_id="teamid",
    bot_access_token="mytoken",
    bot_user_id="mybotuserid"
)
b.save()

# ensure that the bot is in the database
logging.info("Checking for bot in database")
try:
    next(filter(lambda b: b.team_name == "abcde", BotModel.get_bots()))
    logging.info("Found bot successfully")
except sqlite3.OperationalError as e:
    logging.error(e)

# now delete the bot
logging.info("Deleting the bot...")
b.delete()

# ensure the bot is gone
logging.info("Asserting that the bot was deleted...")
try:
    next(filter(lambda b: b.team_name == "abcde", BotModel.get_bots()))
    logging.error("Bot was not deleted.")
except StopIteration:
    logging.info("Bot successfully deleted")

