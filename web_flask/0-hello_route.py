#!/usr/bin/python3
"""
Flask web application
Host `0.0.0.0` port 5000
Route '/' displays "Hello HBNB!"
Makes use of `strict_slashes=false`
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """
    Displays 'Hello HBNB!'
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
