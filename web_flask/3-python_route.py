#!/usr/bin/python3
"""Your web application must be listening on 0.0.0.0, port 5000
    Routes:
    /: display “Hello HBNB!”
    /hbnb: display “HBNB”
    /c/<text>: display “C ” followed by the value of the text variable
    /python/(<text>): display “Python ”, followed by the value of the
    The default value of text is “is cool”
    ou must use the option strict_slashes=False in your route definition
"""
from cgitb import text
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Print Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Print HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """ display “C ” followed by the value of the text variable"""
    new_text = text.replace('_', ' ')
    return "C {}".format(new_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is cool"):
    """ display “Python ” followed by the value of the text variable"""
    new_text = text.replace('_', ' ')
    return "Python {}".format(new_text)

if __name__ == '__main__':
    app.run(host="0.0.0.0")
