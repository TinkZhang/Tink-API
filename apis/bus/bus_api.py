from flask_restx import Namespace, Resource, fields
from apis.bus import bus_data

api = Namespace('bus', description='保利艾庐小区往返地铁站班车信息')

trip = api.model('Trip', {
    'driver': fields.String(required=True, description='司机'),
    'plate': fields.String(required=True, description='车牌号'),
    'color': fields.String(required=True, description='车身颜色'),
    'directionToHome': fields.Boolean(required=True, description='是否回家方向'),
    'leaveTime': fields.String(required=True, description='出发时间'),
    'arriveTime': fields.String(required=True, description='到达时间'),
})

line = api.model('Line', {
    'lineId': fields.String(required=True, discriminator='线路ID'),
    'lineDescription': fields.String(required=True, discriminator='线路描述'),
    'trips': fields.List(fields.Nested(trip)),
})


@api.route("/hello/")
class HelloWorld(Resource):
    def get(self):
        """
        测试
        """
        return "{Hello World!}"


@api.route("/version/")
class Version(Resource):
    def get(self):
        """
        返回班车信息版本号
        """
        return {"version": bus_data.latestVersion}


@api.route("/lines/")
class Lines(Resource):
    @api.expect([line])
    def get(self):
        """
        返回所有班车信息
        """
        return bus_data.lines


@api.route("/line/<line_id>")
@api.doc(params={'line_id': '线路ID'})
class Line(Resource):
    @api.expect(line)
    def get(self, line_id):
        """
        返回指定线路班车信息
        """
        return [line for line in bus_data.lines if line["lineId"] == line_id]
