from flask import Flask
from flask_restx import Resource, Api

from flask_restful import abort,reqparse


app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('task')



TODOS = {
    'todo1': {'task': 'build an API'},
    'todo2': {'task': '哈哈哈'},
    'todo3': {'task': 'profit!'},
}
@api.route('/hello')
class HelloWorld(Resource):
    def get(self):
        return TODOS
    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo'))+1
        todo_id =  'todo%i' % todo_id
        TODOS[todo_id] = {'task':args['task']}
        return TODOS[todo_id],201
if __name__ == '__main__':
    app.run(debug=True)