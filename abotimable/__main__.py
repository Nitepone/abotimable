import coloredlogs
import time
import threading
import logging
from . import server
from . import slackrtm

# install colored logs
coloredlogs.install(level=logging.DEBUG)

# add a filter to all handlers on the root logger that will only permit
# abotimable logs to pass through
for handler in logging.getLogger().handlers:
    handler.addFilter(logging.Filter('abotimable'))


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
