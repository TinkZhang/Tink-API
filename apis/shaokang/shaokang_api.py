from flask_restx import Namespace, Resource, fields
from apis.bus import bus_data

api = Namespace('sk', description='少康战情室音频信息')


@api.route("/version/")
class Version(Resource):
    def get(self):
        """
        返回节目信息版本号
        """
        return {"version": "2024-07-17"}

