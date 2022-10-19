#!usr/bin/python3
"""
    Script that starts a Flask web application
    Your web application must be listening on 0.0.0.0, port 5000
    Routes:
        /: display “Hello HBNB!”
        /hbnb: display “HBNB”
        /c/<text>: display “C ”,
        /python/(<text>)
        /number/<n>
"""

from email.policy import strict
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Return a string"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hello():
    """Return a string"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def hello_text(text):
    """Return a string and a variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)

@app.route('/python/', strict_slashes=False)
@app.route('/python/text', strict_slashes=False)
def hello_python(text='is cool'):
    """Return a string and a variable"""
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)

@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Return a number” only if n is an integer"""
    n = str(n)
    return '{} is a number'.format(n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)