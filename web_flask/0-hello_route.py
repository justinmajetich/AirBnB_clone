#!/usr/bin/python3
"""
A script that starts a Flask web application
listening on 0.0.0.0, port 5000
"""
from flask import Flask

app = Flask("__name__")


@app.route('/', strict_slashes=False)
def hello():
    """Function that displays Hello HBNB!"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
