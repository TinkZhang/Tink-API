from flask import Flask
from apis import api

app = Flask(__name__)
api.init_app(app)


@app.route('/')
def index():
    return {
        "bus_version_url": "https://api.tinks.app/bus/version",
        "bus_all_lines_url": "https://api.tinks.app/bus/lines",
        "bus_line_url": "https://api.tinks.app/bus/{line_id}",
    }
