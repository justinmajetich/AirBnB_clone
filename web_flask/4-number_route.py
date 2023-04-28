#!/usr/bin/python3
"""Define ``0-hello_route`` module. Import Flask
   class and create a new class instance called ``app``.
"""
from flask import Flask


app = Flask('web_flask')


@app.route('/', strict_slashes=False)
def index():
    """Print ``Hello HBNB!``"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """Print 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Display “C ” followed by the value of the text variable

       Argument:
          text: string argument
    """
    return "C {}".format(text.replace('_', ' '))


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python_route(text='is cool'):
    """Display “Python ” followed by the value of the text variable
       Argument:
          text: string argument
    """
    return "Python {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """Display “n is a number” only if n is an integer
       Argument:
         n: integer.
    """
    return "%d is a number" % n


if __name__ == "__main__":
    app.run(host="0.0.0.0")
