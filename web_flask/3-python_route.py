#!/usr/bin/python3
"""starts a Flask web application"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays a string at / route."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """displays a string at /hbnb route."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """displays "C" followed by the value
    of the text variable at /c/<text> route."""
    new = text.replace('_', ' ')
    return 'C %s' % new


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """displays "Python", followed by the value
    of the text variable at /python/(<text>) route."""
    new = text.replace('_', ' ')
    return 'Python %s' % new


if __name__ == "__main__":
    app.run(host='0.0.0.0')
