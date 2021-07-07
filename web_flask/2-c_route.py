#!/usr/bin/python3
""" Start Flask Web Application """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """ Return Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Show HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ Show C with value of variable """
    return 'C ' + text.replace("_", " ")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
