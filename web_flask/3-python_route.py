#!/usr/bin/python3
""" Start flask application
    Must be listening on 0.0.0.0, port 5000
routes:
     /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: Displays 'C' followed by the value of <text>
              Replace underscore _ symbols with a space
    /python/<text>: display “Python ”, followed by the value of <text>
              Replace underscore _ symbols with a space
              The default value of text is “is cool”
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_c_text(text):
    converter = text.replace('_', ' ')
    return f'C {converter}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def show_python_text(text='is cool'):
    converter = text.replace('_', ' ')
    return f'Python {converter}'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
