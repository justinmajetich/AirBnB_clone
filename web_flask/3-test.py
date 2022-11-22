#!/usr/bin/python3
"""
Script that starts a flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Handles appropriate display for index route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def render_hbnb():
    """Handles appropriate display for /hbnb route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Handles appropriate display for /c/:text route """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text='is_cool'):
    """Handles appropriate display for /python/:text route """
    return 'Python %s' % text.replace('_', ' ')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
