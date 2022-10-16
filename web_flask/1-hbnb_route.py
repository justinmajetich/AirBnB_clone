#!/usr/bin/python3
"""a script that starts a Flask web application and return routes"""

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Return a string"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return a string"""
    return 'HBNB'

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)