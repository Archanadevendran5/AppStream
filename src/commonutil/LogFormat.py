import logging
import datetime
from src.commonutil.Config import *

dateTime = datetime.datetime.now().strftime("%m_%d_%Y_%H_%M_%S")
FileName = LogDirectory_Path + f'logs_{dateTime}.log'
File = os.path.expanduser(FileName)


class CustomFormatter(logging.Formatter):
    grey = "\x1b[38;20m"
    yellow = "\x1b[33;20m"
    red = "\x1b[31;20m"
    bold_red = "\x1b[31;1m"
    reset = "\x1b[0m"
    format = "%(asctime)s - %(levelname)s - %(filename)s: %(message)s"

    FORMATS = {
        # logging.DEBUG: grey + format + reset,
        logging.INFO: grey + format + reset,
        logging.WARNING: yellow + format + reset,
        logging.ERROR: red + format + reset,
        logging.CRITICAL: bold_red + format + reset
    }

    def format(self, record):
        log_fmt = self.FORMATS.get(record.levelno)
        formatter = logging.Formatter(log_fmt)
        return formatter.format(record)


logs = logging.getLogger('selenium.webdriver.remote.remote_connection')
logging.basicConfig(filename=File, filemode='w',
                    level=logging.INFO)
logs.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
ch.setFormatter(CustomFormatter())
logs.addHandler(ch)
logs.setLevel(logging.INFO)
logs.warning(f"Log file Created: {File}")
