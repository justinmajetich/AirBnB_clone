#!/usr/bin/python3
""" Starts a Flask web application """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays 'Hello HBNB!' """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Displays 'HBNB' """
    return 'HBNB'


@app.route("/c/<text>")
def C_is_fun(text):
    from markupsafe import escape
    """Display text"""
    text = text.replace('_', ' ')
    return f"C {escape(text)}"


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_is_cool(text="is cool"):
    from markupsafe import escape
    """Display text"""
    text = text.replace('_', ' ')
    return f"Python {escape(text)}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
