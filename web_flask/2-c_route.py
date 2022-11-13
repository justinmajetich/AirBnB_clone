#!/usr/bin/python3
"""starts a Flask web application."""


from flask import Flask


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def helloHBNB():
    """returns Hello HBNB!."""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def HBNB():
    """returns HBNB."""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def variableValue(text):
    """returns the value of a variable."""
    return (text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
