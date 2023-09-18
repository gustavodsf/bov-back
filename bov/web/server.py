import logging
from waitress import create_server
from typing import Union
from bov import config
from bov.core.meta import Singleton
from bov.web import app

class WebServer(metaclass=Singleton):
    
    def __init__(self, host: str, port: Union[str, int]) -> None:
        self.logger = logging.getLogger(__name__)
        self.host = host
        self.port = port
        self.server = create_server(app, host=self.host, port=self.port)
        
    def start(self):
        self.logger.info(f'{config.NAME} - starting web server. HOST={self.host} PORT={self.port}')
        self.server.run()
        
    def stop(self):
        self.logger.info(f'{config.NAME} - stopping web server.')
        self.server.close()
        
web_server = WebServer(config.HTTP_HOST, config.HTTP_PORT)