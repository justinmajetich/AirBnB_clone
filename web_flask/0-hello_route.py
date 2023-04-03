#!/usr/bin/python3
""" a script that starts a Flask web application """
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    return "<p>Hello, world</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
