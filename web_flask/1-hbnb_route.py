#!/usr/bin/python3
"""Flask framework"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """return hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """return HBNB"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
