import os
import sys
import logging


# Bot
TG_HOST = os.getenv('TG_HOST', 'localhost')
TG_TOKEN = os.getenv('TG_TOKEN')
if TG_TOKEN is None:
    raise ValueError('TG_TOKEN is not set')

TG_USE_WEBHOOK = os.getenv('TG_USE_WEBHOOK', 'false').lower() == 'true'


# Logging
LOG_DIR = os.getenv('LOG_DIR',
                    f'/var/log/{os.path.basename(sys.argv[0])}')

if not os.path.exists(LOG_DIR):
    os.mkdir(LOG_DIR)

logFormatter = logging.Formatter("%(asctime)s [%(threadName)-0.12s] [%(levelname)-0.5s] %(message)s")

fileHandler = logging.FileHandler("{0}/{1}.log".format(LOG_DIR, "bot"))
fileHandler.setFormatter(logFormatter)

rootLogger = logging.getLogger()
rootLogger.addHandler(fileHandler)
rootLogger.setLevel(logging.INFO)

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(logFormatter)
rootLogger.addHandler(consoleHandler)
