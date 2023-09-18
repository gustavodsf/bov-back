import os
import configparser

from dataclasses import dataclass, fields

parser = configparser.ConfigParser()
parser.read('settings.ini')

@dataclass(frozen=True)
class Configuration:

    LOGGING_CONFIG_FILE: str = os.environ.get('LOGGING_CONFIG_FILE', parser.get('system', 'LOGGING_CONFIG_FILE'))
    HTTP_HOST: str = os.environ.get('HTTP_HOST', parser.get('web', 'HTTP_HOST'))
    HTTP_PORT: str = os.environ.get('HTTP_PORT', parser.get('web', 'HTTP_PORT'))
    NAME: str = os.environ.get('NAME', parser.get('application', 'NAME'))
    VERSION: str = os.environ.get('VERSION', parser.get('application', 'VERSION'))

    POSTGRES_HOST: str = os.environ.get('POSTGRES_HOST', parser.get('db', 'POSTGRES_HOST'))
    POSTGRES_PORT: str = os.environ.get('POSTGRES_PORT', parser.get('db', 'POSTGRES_PORT'))
    POSTGRES_USER: str = os.environ.get('POSTGRES_USER', parser.get('db', 'POSTGRES_USER'))
    POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD', parser.get('db', 'POSTGRES_PASSWORD'))
    POSTGRES_DB: str = os.environ.get('POSTGRES_DB', parser.get('db', 'POSTGRES_DB'))

    SQLALCHEMY_DATABASE_URI: str = os.environ.get('SQLALCHEMY_DATABASE_URI', parser.get('db', 'SQLALCHEMY_DATABASE_URI'))
    SECRET_KEY: str = os.environ.get('SECRET_KEY', parser.get('db', 'SECRET_KEY'))
    
    def __post_init__(self):
        
        for field in fields(self):

            if not isinstance(value := getattr(self, field.name), field.type):
                object.__setattr__(self, field.name, field.type(value))

