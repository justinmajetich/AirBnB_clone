#!/usr/bin/python3

"""
Script that starts a Flask web application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET'], strict_slashes=False)
def hello_hbnb():
    """Returns a greeting message"""
    return "Hello HBNB!"


@app.route('/hbnb', methods=['GET'], strict_slashes=False)
def hbnb():
    """Returns the acronym HBNB"""
    return "HBNB"


@app.route('/c/<string:text>', methods=['GET'], strict_slashes=False)
def text_route(text):
    """Returns the text after the letter 'C' """
    return "C {}".format(text.replace("_", " "))


@app.route('/python', methods=['GET'], strict_slashes=False)
@app.route('/python/<string:text>', methods=['GET'], strict_slashes=False)
def text_route_python(text="is cool"):
    """Returns the text after the word 'Python'"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', methods=['GET'], strict_slashes=False)
def num_route(n):
    """Returns a message stating that the given input is a number"""
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>', methods=['GET'], strict_slashes=False)
def num_template(n):
    """Renders a template that displays the given number"""
    return render_template("5-number.html", n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
