from flask import Flask

import bus_data

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/version")
def version():
    return {"version": f"{bus_data.latestVersion}"}


@app.route("/lines")
def lines():
    return bus_data.lines


@app.route("/line/<line_id>")
def line(line_id):
    return [line for line in bus_data.lines if line["lineId"] == line_id]
