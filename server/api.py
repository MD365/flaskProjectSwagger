#server api.py
from flask import Blueprint
from flask_restx import Api
from server.apis.test.web import ns as test_ns


api_v1 = Blueprint('api1',__name__,url_prefix='/api')

api = Api(
    api_v1,
    version='1.0',
    title='test flask',
    description='test flask',
)

api.add_namespace(test_ns)

