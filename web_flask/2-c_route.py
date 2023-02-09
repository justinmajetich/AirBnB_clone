#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """Funtion to print Hello HBNB"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """print HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """print the value of text"""
    return "C {}".format(text).replace("_", " ")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
