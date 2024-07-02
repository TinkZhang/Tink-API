from flask import Flask
from flask_restx import Api
from flask_restx import Namespace, Resource, fields
import bus_data

app = Flask(__name__)

api = Api(
    title='Tink\'s API',
    version='1.0',
    description='These APIs are designed for my hobby projects',
    doc='/docs/'
)

ns_bus = Namespace('bus', description='保利艾庐小区往返地铁站班车信息')

trip = ns_bus.model('Trip', {
    'driver': fields.String(required=True, description='司机'),
    'plate': fields.String(required=True, description='车牌号'),
    'color': fields.String(required=True, description='车身颜色'),
    'directionToHome': fields.Boolean(required=True, description='是否回家方向'),
    'leaveTime': fields.String(required=True, description='出发时间'),
    'arriveTime': fields.String(required=True, description='到达时间'),
})

line = ns_bus.model('Line', {
    'lineId': fields.String(required=True, discriminator='线路ID'),
    'lineDescription': fields.String(required=True, discriminator='线路描述'),
    'trips': fields.List(fields.Nested(trip)),
})

api.add_namespace(ns_bus)
api.init_app(app)
# app.run()


@ns_bus.route("/hello/")
class HelloWorld(Resource):
    def get(self):
        """
        测试
        """
        return "{Hello World!}"


@ns_bus.route("/version/")
class Version(Resource):
    def get(self):
        """
        返回班车信息版本号
        """
        return {"version": bus_data.latestVersion}


@ns_bus.route("/lines/")
class Lines(Resource):
    @api.expect([line])
    def get(self):
        """
        返回所有班车信息
        """
        return bus_data.lines


@ns_bus.route("/line/<line_id>")
@api.doc(params={'line_id': '线路ID'})
class Line(Resource):
    @api.expect(line)
    def get(self, line_id):
        """
        返回指定线路班车信息
        """
        return [line for line in bus_data.lines if line["lineId"] == line_id]
