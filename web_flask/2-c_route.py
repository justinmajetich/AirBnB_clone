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


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """display C, followed by the value of the text variable"""
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
