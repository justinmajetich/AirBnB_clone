#!/usr/bin/python3
""" Write a script that starts a Flask web application
"""
from flask import Flask, escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ display “Hello HBNB!”"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """/hbnb: display “HBNB”"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C(text):
    """/c/<text>: display “C ” followed by the value of the text variable
    """
    
    return 'C %s' % text.replace(text)


@app.route('/python', strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def PYTHON(text = "is cool"):
    """
    /python/(<text>): display “Python ”, followed by the value of the text variable
    """
    return 'Python %s' % text.replace("_", " ")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
