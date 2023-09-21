#!/usr/bin/python3
""" 
    A script that starts a Flask web application listening
    on 0.0.0.0, port 5000 with Routes [/]: display “Hello HBNB!”,
    [/hbnb]: display “HBNB” and [/c/<text>]: display “C”
     followed by the value of the text variable
"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ [/]: display “Hello HBNB!” """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ [/hbnb]: display “HBNB” """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def Cpage(text):
    """ [/c/<text>]: display “C” plus the value of text """
    msg = f"C {escape(text).replace('_', ' ')}"
    return msg


if __name__ == '__main__':
    """ Run module only then ran """
    app.run(host='0.0.0.0', port=5000)
