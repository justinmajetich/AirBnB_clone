#!/usr/bin/python3
"""Script that starts a Flask web app must be listening on 0.0.0.0port 5000"""

from flask import Flask, escape

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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route handler for the '/c/<text>' URL.

    Args:
        text (str): The text provided in the URL.

    Returns:
        str: The string "C " followed by the value of the text variable.
    """
    return "C {}".format(escape(text.replace("_", " ")))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
