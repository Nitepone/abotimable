import threading
import logging

from . import server
from . import slackrtm

def server_monitor():
    while True:
        try:
            server.app.run(host="0.0.0.0", port=5000)
        except Exception as e:
            logging.error("Server thread died")
            logging.error(e)

def slack_monitor():
    while True:
        try:
            slackrtm.main()
        except Exception as e:
            logging.error("Slack thread died")
            logging.error(e)

threading.Thread(target=slack_monitor).start()
threading.Thread(target=server_monitor).start()
