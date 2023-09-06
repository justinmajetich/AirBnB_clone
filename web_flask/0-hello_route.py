#!/usr/bin/python3
"""Script that start a Flask webapp"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hell():
    """function to return a string"""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
