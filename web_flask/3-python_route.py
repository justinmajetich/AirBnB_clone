#!/usr/bin/python3
"""Flask web application script."""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Returns 'Hello HBNB!'."""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns 'HBNB'."""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Returns 'C ' followed by the modified text."""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Returns 'Python ' followed by the modified text or default string."""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


if __name__ == '__main__':
    """Runs the script if not imported."""
    app.run(host='0.0.0.0', port=5000)
