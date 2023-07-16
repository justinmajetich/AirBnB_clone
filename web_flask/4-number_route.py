#!/usr/bin/python3
"""
script that starts a Flask web application

Your web application must be listening on 0.0.0.0, port 5000

Routes:
/: display “Hello HBNB!”
/hbnb: display “HBNB”
/c/<text>:
    display “C ” followed by
    the value of the text variable
        (replace underscore _ symbols with a space )
/python/<text>:
    display “Python ”, followed by
    the value of the text variable
        (replace underscore _ symbols with a space )
    default value of text is “is cool”

/number/<n>:
    display “n is a number”
        only if n is an integer
        replace "n" with the int given

You must use the option strict_slashes=False in your route definition.
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_():
    """if rout as above,
    returns as below
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """if rout as above,
    returns as below
    """
    return 'HBNB'


@app.route('/c/<text>')
def hello_c_text(text=''):
    """if rout as above,
    returns as below
    """
    edited = text.replace('_', ' ')
    return 'C ' + edited


@app.route('/python')
@app.route('/python/')
@app.route('/python/<text>')
def hello_python_text(text='is cool'):
    """if rout as above,
    returns as below
    """
    edited = text.replace('_', ' ')
    return 'Python ' + edited


@app.route('/number/<int:n>')
def hello_number(n=0):
    """if n is int, return it is a number
    """
    return str(n) + ' is a number'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
