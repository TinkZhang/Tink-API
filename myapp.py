from flask import Flask
from apis import api

app = Flask(__name__)


# api.init_app(app)
# app.run()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
