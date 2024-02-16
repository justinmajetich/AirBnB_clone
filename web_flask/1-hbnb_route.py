#!/usr/bin/python3
"""
Start a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """ Display Hello HBNB! """
    return "HBNB"


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port)
