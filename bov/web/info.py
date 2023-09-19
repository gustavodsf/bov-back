from flask_restx import Namespace,Resource, fields
from bov import config
from datetime import datetime

api = Namespace('api/info', description='health check')

info = api.model('Info', {
    'app': fields.String(readonly=True, description='application name'),
    'version': fields.String(required=True, description='application version'),
    'time': fields.String(required=True, description='current time')
})

@api.route('/')
class Info(Resource):

    @api.doc('get_info')
    @api.marshal_with(info, code=200)
    def get(self) -> dict:
      return {
          'app': config.NAME,
          'version': config.VERSION,
          'time': str(datetime.now())
      }