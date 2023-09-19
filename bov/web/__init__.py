from flask import Flask, render_template, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_restx import Api, Resource, fields

from bov import config
import bov.core.utils as utils
from .info import api as info_api

app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = config.SQLALCHEMY_DATABASE_URI
app.config['SECRET_KEY'] = config.SECRET_KEY

CORS(app, resources={r"/*": {"origins": "http://localhost:3000",
                                "methods": ["GET", "POST", "PATCH", "DELETE"],
                                "supports_credentials": True}})
db = SQLAlchemy()
migrate = Migrate()
db.app = app
db.init_app(app)

migrate.init_app(app, db)
utils.csrf.init_app(app)


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

api.add_namespace(info_api)

app.register_error_handler(Exception, handle_error)


