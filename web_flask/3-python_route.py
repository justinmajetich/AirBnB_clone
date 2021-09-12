#!/usr/bin/python3
"""
    script that starts a Flask web application
"""

from flask import Flask, escape, request

# creates instance of Flask, app is bound to gunicorn when running app server
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        Hello route
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def index():
    """
        Index route
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_show(text):
    """
        Show c text
    """
    text = str(text).replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python', strict_slashes=False, defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_show(text):
    """
        Show python text
    """
    text = str(text).replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    # runs the Flask application through port 5000 from local host
    app.run(host='0.0.0.0', port='5000')
