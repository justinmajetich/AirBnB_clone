#!/usr/bin/python3
from flask import Flask
"""Task 0 for Flask Project"""
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Returns Hello HBNB for the '/' url"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
