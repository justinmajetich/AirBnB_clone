#!/usr/bin/python3
"""Write a script that starts a Flask web app which must be listening on 0.0.0.0"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL ('/').

    Returns:
        str: A simple greeting message.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the '/hbnb' URL.

    Returns:
        str: The string "HBNB".
    """
    return "HBNB"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
