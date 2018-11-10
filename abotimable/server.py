import configparser
import pystache
import logging
from flask import request
from slackclient import SlackClient

from abotimable import app, slackrtm
from abotimable.model import bot as bot_model

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

# read in the templates
with open('templates/index.mustache') as fh:
    index_template = fh.read()

with open('templates/success.mustache') as fh:
    success_template = fh.read()

with open('templates/status.mustache') as fh:
    status_template = fh.read()

config = configparser.RawConfigParser()
config.read('config.ini')

client_id = config['SLACK']['CLIENT_ID']
client_secret = config['SLACK']['CLIENT_SECRET']
oauth_scope = config['SLACK']['OAUTH_SCOPE']
oauth_redirect = config['SLACK']['OAUTH_REDIRECT']


@app.route("/", methods=["GET"])
def pre_install():
    return pystache.render(index_template, {
        "oauth_redirect": oauth_redirect,
        "oauth_scope": oauth_scope,
        "client_id": client_id
    })


@app.route("/callback", methods=["GET", "POST"])
def post_install():

    # Retrieve the auth code from the request params
    auth_code = request.args['code']

    # An empty string is a valid token for this request
    sc = SlackClient("")

    # Request the auth tokens from Slack
    auth_response = sc.api_call(
      "oauth.access",
      client_id=client_id,
      client_secret=client_secret,
      redirect_uri=oauth_redirect,
      code=auth_code
    )

    logger.debug(auth_response)

    assert isinstance(auth_response, dict)
    assert auth_response['ok'] == True
    assert 'bot' in auth_response, \
        "You may need to add bot permissions to your app"

    b = bot_model.Bot(
        bot_user_id=auth_response['bot']['bot_user_id'],
        bot_access_token=auth_response['bot']['bot_access_token'],
        team_name=auth_response['team_name'],
        team_id=auth_response['team_id'],
    )
    b.save(callback=slackrtm.start_bot_monitor)

    return pystache.render(success_template, {})

@app.route("/status", methods=["GET"])
def status():
    return pystache.render(status_template, {
        'teams': map(lambda bot: {"name": bot.team_name}, bot_model.get_bots())
    })

if __name__ == "__main__":
    run()
