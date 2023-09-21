#!/usr/bin/python3
""" 
    A script that starts a Flask web application listening
    on 0.0.0.0, port 5000 with Routes:
    [/]:              display “Hello HBNB!
    [/hbnb]:          display “HBNB”
    [/c/<text>]:      display “C”
        followed by the value of the text variable
    [/python/<text>]: display “Python”
        followed by the value of the text variable with
        default value of text set as “is cool”
    [/number/<n>]:    display “n is a number”
        only if n is an integer
"""

from flask import Flask, render_template
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

@app.route('/python', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def PYpage(text='is cool'):
    """ [/python/<text>]: display “Python” plus the value of text """
    msg = f"Python {escape(text).replace('_', ' ')}"
    return msg

@app.route('/number/<int:n>', strict_slashes=False)
def Npage(n):
    """ [/number/<n>]: display “n is a number” only if n is an integer """
    msg = f"{n} is a number"
    return msg

@app.route('/number_template/<int:n>', strict_slashes=False)
def run_tmplt(n):
    """ [/number/<n>]: display “n is a number” only if n is an integer """
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    """ Run module only then ran """
    app.run(debug=True ,host='0.0.0.0', port=5000)
