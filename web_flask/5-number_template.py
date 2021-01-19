#!/usr/bin/python3
""" Start Flask Web Application """
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """ Return Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Show HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """ Show C with value of variable """
    return 'C ' + text.replace("_", " ")


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_route(text="is cool"):
    """ display Python, and variable """
    return "Python" + " " + text.replace("_", " ")


@app.route("/number/<int:n>", strict_slashes=False)
def number_route(n):
    """ Display n if n is integer"""
    if type(n) == int:
        return str(n) + " is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template_route(n):
    """ varible sends a numeric in HTML """
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
