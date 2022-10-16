#!/usr/bin/python3
""" A script that starts a Flask web application
    Listen on 0.0.0.0, port 5000
    Routes: 
            /: display “Hello HBNB!”
            /hbnb: display “HBNB”
            /c/<text>
"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """Return a string"""
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hello():
    """Return stirng"""
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Return a string with variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000)