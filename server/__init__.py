# server  __init__.py
from flask import Flask

def create_app():
    # 创建Flask对象
    app = Flask(__name__)
    # 注册蓝图
    from server.api import api_v1
    app.register_blueprint(api_v1)
    return app