from abotimable.model import bot as bot_model
import configparser
import sqlite3
import pystache
import logging
from flask import Flask, request
from slackclient import SlackClient

logging.basicConfig(level=logging.DEBUG)

# read in the template
with open('templates/index.mustache') as fh:
    index_template = fh.read()

app = Flask(__name__)

config = configparser.RawConfigParser()
config.read('config.ini')

client_id = config['SLACK']['CLIENT_ID']
client_secret = config['SLACK']['CLIENT_SECRET']
oauth_scope = config['SLACK']['OAUTH_SCOPE']
oauth_redirect = "http://localhost:5000/callback"


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
      redirect_url=oauth_redirect,
      code=auth_code
    )

    logging.debug(auth_response)

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
    b.save()

    # return something
    return "Success!"
