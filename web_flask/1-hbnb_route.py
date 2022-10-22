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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
