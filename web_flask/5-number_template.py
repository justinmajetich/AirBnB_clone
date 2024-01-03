#!/usr/bin/python3

"""
Starts a Flask web application.
    /number_template/<n>: Displays an HTML page only if <n> is an integer.
        - Displays the value of <n> in the body.
"""

from flask import Flask, render_template

""" Creates an application object """
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ returns Hello HBNB """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Returns 'HBNB' """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """ Displays 'C' followed by the value of <text> """
    replaced = text.replace("_", " ")
    return f"C {replaced}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """ Displays 'Python' followed by the value of <text> """
    replaced = text.replace("_", " ")
    return f"Python {replaced}"


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """ Display 'n is a number' only if n is an integer """
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """ Display 'n is a number' only if n is an integer """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
