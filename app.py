from flask import Flask
# from flask_restful import Resource
from flask_restful import abort,reqparse
from flask_restx import Api,Resource,fields
app = Flask(__name__)
api = Api(app,version='1.0',title='中文标题',description='这个API的描述')
#模块明明空间
ns = api.namespace('Todo',description='描述')


#返回值模型
todo = api.model('Todo', {
    'id': fields.Integer(readonly=True, description='The task unique identifier'),
    'task': fields.String(required=True, description='The task details')
})

TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '哈哈哈'},
    'todo3': {'task': 'profit!'},
}


def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404,message="todo {} doesn exist".format(todo_id))

#参数模型
parser = reqparse.RequestParser()
parser.add_argument('task')

# @api.route('/todos/<todo_id>')
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        return TODOS[todo_id]

    def delete(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
        del TODOS[todo_id]
        return '', 204

    def put(self, todo_id):
        args = parser.parse_args()
        task = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201
# @api.route('/todos')
class TodoList(Resource):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.params = parser.parse_args()

    @ns.expect(parser)
    @ns.response(200,"成功返回",todo)
    def get(self):
        return TODOS

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo'))+1
        todo_id =  'todo%i' % todo_id
        TODOS[todo_id] = {'task':args['task']}
        return TODOS[todo_id],201
#
# api.add_resource(TodoList,'/todos')
api.add_resource(Todo,'/todos/<todo_id>')
ns.add_resource(TodoList,"/todos")
if __name__ == '__main__':
    app.run(debug=True,port='10086')