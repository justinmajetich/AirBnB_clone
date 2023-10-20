#!/usr/bin/python3
"""
This is a script that starts a Flask web application
"""

from flask import Flask, abort

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Display 'Hello HBNB!'
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def say_hbnb():
    """
    Display the text 'HBNB'
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """
    Display 'C' followed by the text variable
    """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def display_py(text):
    """
    Display 'Python' followed by the text variable
    """
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<n>", strict_slashes=False)
def display_num(n):
    """
    Display 'n' is number if n is int
    """
    try:
        x = int(n)
        return "{} is a number".format(x)
    except ValueError:
        abort(404)
    


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
