import configparser, sqlite3, pystache, logging
from flask import Flask, request
from slackclient import SlackClient

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
  access_token = auth_response['access_token']

  # return something
  return "Success!"
