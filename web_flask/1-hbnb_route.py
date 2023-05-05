#!/usr/bin/python3
"""
This scrip handles request to multi URL paths
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Handles requests to root URL

    Returns:
        dtr: Greetings
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Handles request for HBNB

    Returns:
        str: HBNB
    """
    return 'HBNB'


if __name__ == '__main__':
    """
    serve page on below port
    """
    app.run(host='0.0.0.0', port=5000)
