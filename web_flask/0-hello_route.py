#!/usr/bin/python3
"""Imports the Flask class from the flask,used to create Flask web app"""


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL ('/')
    Returns:
    str: A simple greeting message.
    """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
