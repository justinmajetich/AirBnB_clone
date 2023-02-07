#!/usr/bin/python3
"""Definition of a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """
    The hello_world function returns the string 'Hello HBNB!'
    :return: The string `Hello HBNB!`
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """
    The hbnb function returns the string 'HBNB'
    :return: The string `HBNB`
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """
    The c_text function returns the string 'C + {text}'
    :return: The string `C + {text}`
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def pyth(text="is cool"):
    """
    The pytee function returns the string 'Python + {text}'
    :return: The string `Python + {text}`
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:num>", strict_slashes=False)
def number(num):
    """
    The number function returns the string 'n is a number'
    :return: `n is a number`
    """
    return "{} is a number".format(num)


@app.route("/number_template/<int:numb>", strict_slashes=False)
def number_template(numb):
    """
    The number_template function renders a HTML file
    :return: 5-number.html..
    """
    return render_template("5-number.html", numb=numb)


@app.route("/number_odd_or_even/<int:numb>", strict_slashes=False)
def odd_even(numb):
    """
    The odd_even function renders a HTML file
    :return: 6-number_odd_or_even.html
    """
    return render_template("6-number_odd_or_even.html", numb=numb)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
