from flask_restx import Resource, fields, Namespace

api = Namespace('api/animal', description='Animal related operations')

animal = api.model('Animal', {
})


@api.route('/')
class AnimalListOrCreate(Resource):
  '''Shows a list of all Animals, and lets you POST to add new Animal'''
  @api.doc('list_animais')
  @api.marshal_list_with(animal)
  def get(self):
      '''List all tasks'''
      return []

  @api.doc('create_animal')
  @api.expect(animal)
  @api.marshal_with(animal, code=201)
  def post(self):
      '''Create a new task'''
      return {}


@api.route('/<int:id>')
@api.response(404, 'Animal not found')
@api.param('id', 'The animal identifier')
class AnimalFilterDeleteUpdate(Resource):
  '''Show a single animal item and lets you delete them'''
  @api.doc('get_animal')
  @api.marshal_with(animal)
  def get(self, id):
      '''Fetch a given resource'''
      return {}

  @api.doc('delete_animal')
  @api.response(204, 'animal deleted')
  def delete(self, id):
      '''Delete a animal given its identifier'''
      return '', 204

  @api.expect(animal)
  @api.marshal_with(animal)
  def put(self, id):
      '''Update a task given its identifier'''
      return {}