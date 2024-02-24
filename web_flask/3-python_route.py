#!/usr/bin/python3
"""
Start a Flask web application
"""

from flask import Flask

app = Flask(__name__)


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def hello_hbnb_python(text="is cool"):
    """ Display Hello HBNB! """
    if not text:
        text = "is cool"
    return "Python {}".format(text.replace("_", " "))


if __name__ == "__main__":
    host = '0.0.0.0'
    port = 5000
    app.run(host=host, port=port)
