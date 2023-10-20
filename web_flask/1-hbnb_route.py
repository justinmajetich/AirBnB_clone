#!/usr/bin/python3
"""
This module define a flask web framework with a route
"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """display hello hbnb"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """This function define the route"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
