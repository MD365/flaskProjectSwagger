import json
from flask import request,render_template,make_response,jsonify
from flask_restx import Namespace,Resource,fields

ns = Namespace('test',description='test')

@ns.route("",strict_slashes=False)#实际访问地址/api/test/
class TestHandler(Resource):

    def get(self):
        # 如果使用模板的块，需要使用 make_response
        # return make_response(render_template('index.html', data=res), 200)

        # 使用 jsonify 是为了返回json数据的同时，相比于 json.dumps() 其会自动修改 content-type 为 application/json
        # 另外，如果使用 jsonify()的同时，还想自定义返回状态码，可以使用 make_response(jsonify(data=data), 201)
        return jsonify()

    def post(self):
        pass

    def put(self):
        pass

    def delete(self):
        pass

@ns.route("/<id>",strict_slashes=False)#实际访问地址/api/test/1
@ns.doc(params={'id':'an id'})
class TestHandler(Resource):

    def get(self,id):
        return jsonify()

    @ns.doc(response={403:"not authorized"})
    def post(self,id):
        pass


parent = ns.model('Parent', {
    'name': fields.String,
    'age': fields.Integer(discriminator=True),
    'addr': fields.String(description='地址'),
    'gender': fields.String(description='性别', required=True, enum=['男', '女', '未知'])
})

child = ns.inherit('Child', parent, {
    'extra': fields.String
})


@ns.route("/test3", strict_slashes=False)  # /api/test/test3
class Test2Handler(Resource):

    @ns.marshal_with(child, as_list=True)  # 等价于 @api.marshal_list_with(resource_fields)
    def get(self):
        return "返回一个对象"

    @ns.marshal_with(child, code=201)  # 201 代表创建成功
    def post(self):
        return '创建一个对象成功', 201