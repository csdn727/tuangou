import logging
from logging import CRITICAL, DEBUG, ERROR, FATAL, INFO, NOTSET, WARN, WARNING
from util import getPath

log_level = INFO
log_path = getPath()


def singleton(cls):
    instances = {}

    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance


@singleton
class Logger(object):

    def __init__(self):

        logger = logging.getLogger()
        FORMAT = "[%(asctime)s][%(filename)s:%(lineno)d][%(funcName)s][%(levelname)s] %(message)s"
        hdlr = logging.FileHandler(log_path + 'tuangou.log')
        logging.basicConfig(format=FORMAT)
        formatter = logging.Formatter(FORMAT)
        hdlr.setFormatter(formatter)
        logger.addHandler(hdlr)
        logger.setLevel(log_level)

        self.logger = logger

    def getLogger(self):
        return self.logger
