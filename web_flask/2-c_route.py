#!/usr/bin/python3
"""a script that starts a Flask web application
and listens on 0.0.0.0, port 5000"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """returns a string at the root route"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """displays "C" followed by the value
    of the text variable at /c/<text> route."""
    new = text.replace('_', ' ')
    return 'C %s' % new


if __name__ == "__main__":
    app.run(host='0.0.0.0')
