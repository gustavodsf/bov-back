import logging.config

from bov.config import Configuration


config = Configuration()

logging.config.fileConfig(fname=f'{config.LOGGING_CONFIG_FILE}')