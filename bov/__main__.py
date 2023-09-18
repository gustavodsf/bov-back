import logging
import logging.config
import os
import signal
import sys
import time

from bov import config
from bov.web.server import web_server


if __name__ == '__main__':

  logger = logging.getLogger(__name__)
  logger.info(f'{config.NAME} - application starting...')

  def start() -> None:
    web_server.start()
    while True:
        time.sleep(1)

  def stop() -> None:
      web_server.stop()

  def signal_handler(sig, frame) -> None:
      logger.debug(f'{config.NAME} - signal received: {signal.Signals(sig).name}.')
      logger.info(f'{config.NAME} - stopping application.')
      stop()
      logger.info(f'{config.NAME} - bye bye.')
      try:
          sys.exit(0)
      except SystemExit:
          os._exit(0)

  signal.signal(signal.SIGINT, signal_handler)
  signal.signal(signal.SIGTERM, signal_handler)
    
  start()