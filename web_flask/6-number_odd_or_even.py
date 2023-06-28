#!/usr/bin/python3
""" Web application listening on the 0.0.0.0, port 5000 """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """ Displays Hello HBNB! on home route """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb_route():
    """ Displays HBNB! on hbnb route """
    return "HBNB"


@app.route("/c/<text>")
def c_route(text):
    """
    Displays 'C' followed by the value of text
    Replaces underscores with a space
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/")
@app.route("/python/<text>")
def python_route(text="is cool"):
    """
    Displays 'python' followed by the value of text
    Replaces underscores with a space
    """
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>')
def number_route(n):
    """
    Displays 'number' followed by the value of text
    only if n is a number
    """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def template_route(n):
    """
    Displays an html page
    only if n is a number
    """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>')
def template_number_route(n):
    """
    Displays an html page
    whether n is odd or even
    """
    res = ""
    if isinstance(n, int):
        if n % 2 == 0:
            res = "even"
        else:
            res = "odd"
        return render_template("6-number_odd_or_even.html", number=n, result=res)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    app.url_map.strict_slashes = False
