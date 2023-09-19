from flask import Flask, render_template, request
from flask_cors import CORS
from flask_restx import Api, Resource, fields

from bov import config
import bov.core.utils as utils

from .database import db, migrate

## Swagger Namespace
from .info import api as info_api
from bov.animal.animal_controller import api as animal_api
from bov.tarefa.tarefa_controller import api as tarefa_api
## Swagger Namespace

## Migration - Import so that the models are created
from bov.animal.animal import Animal
from bov.tarefa.tarefa import Tarefa
## Migration


app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = config.SECRET_KEY

CORS(app, resources={r"/*": {"origins": "http://localhost:3000",
                                "methods": ["GET", "POST", "PATCH", "DELETE"],
                                "supports_credentials": True}})

utils.csrf.init_app(app)

## Migration
db.app = app
db.init_app(app)
migrate.init_app(app, db)
## Migration


api = Api(app, version= config.VERSION, title=config.NAME,description=config.NAME,)

@app.errorhandler(404)
def handle_not_found_error(e):
    response = {
        'status': 'fail',
        'message': f"route: '{request.path}' not found on this server"
    }
    return response, 404


def handle_error(error):
    response = {
        'status': 'error',
        'message': str(error)
    }
    return response, 500


## Swagger Namespace
api.add_namespace(info_api)
api.add_namespace(animal_api)
api.add_namespace(tarefa_api)
## Swagger Namespace

app.register_error_handler(Exception, handle_error)


