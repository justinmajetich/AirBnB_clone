#!/usr/bin/python3
""" Web application listening on 0.0.0.0, port 5000 """
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """ Display Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ Display HBNB! """
    return "HBNB"


@app.route("/c/<text>")
def c_is_fun(text):
    """
    Display 'C' followed by the value of text
    Replace underscore _ symbols with a space
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/")
@app.route("/python/<text>")
def python_is_cool(text="is cool"):
    """
    Display 'Python' followed by the value of text
    Replace underscore _ symbols with a space
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>")
def number(n):
    """
    Display 'n is a number' only if n is an integer
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>")
def number_template(n):
    """
    Display a HTML page only if n is an integer
    """
    return render_template('5-number.html', n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even_template(n):
    """
    Display a HTML page only if n is an integer
    Number: n is even|odd
    """
    return render_template('6-number_odd_or_even.html', n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    app.url_map.strict_slashes = False
