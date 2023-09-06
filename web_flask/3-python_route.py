#!/usr/bin/python3
"""Script that start a Flask webapp"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hell():
    """function to return a string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hello_hbnb():
    """prints hbnb"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    """"replace _ with spaces"""
    text = text.replace('_', ' ')
    return f"c {text}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is_cool"):
    """print is cool"""
    if text is not 'is cool':
        text = text.replace('_', ' ')
    return f"Python {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
