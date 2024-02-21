#!/usr/bin/python3

"""
Simple flask server with three end points /,  /hbnb and /c
and listens on port 5000
"""

from flask import Flask, render_template

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


@app.route("/number_template/<int:n>", strict_slashes=False)
def is_number_template(n):
    """route to /number_template
    Return a template if n is an interger
    """
    if isinstance(n, int):
        return render_template("5-number.html", number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """
    Route to /number_odd_or_even/ return a template
    indicating in n is odd or even
    """
    if isinstance(n, int):
        if n % 2 == 0:
            text = "Number: {} is even".format(n)
        else:
            text = "Number: {} is odd".format(n)
        return render_template("6-number_odd_or_even.html", text=text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
