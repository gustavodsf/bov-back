from flask_restx import Resource, fields, Namespace

api = Namespace('api/tarefa', description='Tarefa related operations')

tarefa = api.model('tarefa', {
})


@api.route('/')
class TarefaListOrCreate(Resource):
  '''Shows a list of all tarefas, and lets you POST to add new tarefa'''
  @api.doc('list_animais')
  @api.marshal_list_with(tarefa)
  def get(self):
      '''List all tasks'''
      return []

  @api.doc('create_tarefa')
  @api.expect(tarefa)
  @api.marshal_with(tarefa, code=201)
  def post(self):
      '''Create a new task'''
      return {}


@api.route('/<int:id>')
@api.response(404, 'tarefa not found')
@api.param('id', 'The tarefa identifier')
class TarefaFilterDeleteUpdate(Resource):
  '''Show a single tarefa item and lets you delete them'''
  @api.doc('get_tarefa')
  @api.marshal_with(tarefa)
  def get(self, id):
      '''Fetch a given resource'''
      return {}

  @api.doc('delete_tarefa')
  @api.response(204, 'tarefa deleted')
  def delete(self, id):
      '''Delete a tarefa given its identifier'''
      return '', 204

  @api.expect(tarefa)
  @api.marshal_with(tarefa)
  def put(self, id):
      '''Update a task given its identifier'''
      return {}