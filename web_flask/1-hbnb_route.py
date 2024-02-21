#!/usr/bin/python3

"""
Simple flask server with two end points / and /hbnb
and listens on port 5000
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_holberton():
    """
    route to / to Display Hello HBNB on any request
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb_route():
    """
    Route to /hbnb to display HBNB on any request
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
