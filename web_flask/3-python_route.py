#!/usr/bin/python3
"""
Task 1 for Flask Project Web Framework
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """
    Returns Hello HBNB for the '/' url
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb_route():
    """
    Returns HBNB for the /hbnb route
    """
    return "HBNB"


@app.route('/python/<text>', strict_slashes=False)
def python_is_magic(text):
    """Display Python, followed by the value of the text"""
    if text is None:
        return "Python is cool"
    return f"Python {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
