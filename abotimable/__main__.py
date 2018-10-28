import threading

from . import server
from . import slackrtm

server_thread = threading.Thread(target=server.app.run, kwargs={
    "host": "0.0.0.0",
    "port": 5000
})
server_thread.start()

slack_thread = threading.Thread(target=slackrtm.main)
slack_thread.start()
