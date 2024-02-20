#!/usr/bin/python3
""" Starts a new Flask web application. """

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_hbnb():
    """ Return the text Hello HBNB! """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
