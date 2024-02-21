#!/usr/bin/python3

"""
Simple flask server with three end points /,  /hbnb and /c
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


@app.route("/c/<string:text>", strict_slashes=False)
def c_is_fun(text):
    """Route to /c to display 'C' followed by text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", strict_slashes=False)
@app.route("/python/<string:text>", strict_slashes=False)
def python_is(text="is cool"):
    """Route to /c to display 'C' followed by text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
    """ Route to /number to dispaly n, if its an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
