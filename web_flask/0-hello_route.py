#!/usr/bin/python3
"""0-hello_route module"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Starts a Flask web application
    Return: Hello HBNB!
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
