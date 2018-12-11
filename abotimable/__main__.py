import time
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
        logging.info("Waiting 5 seconds before restarting server thread")
        time.sleep(5)


threading.Thread(target=server_monitor).start()

slackrtm.main()
