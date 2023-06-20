#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbn():
    """ Return Hello HBNB! from 0.0.0.0:5000 """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0')
