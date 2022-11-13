#!/usr/bin/python3
"""
starts a Flask web application
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """return Hello HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hello_HNNB():
    """return HBNB"""
    return 'HBNB!'


@app.route('/c/<text>', strict_slashes=False)
def hello_txt(text):
    """return the text"""
    return 'C ' + text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_txt(text='is cool'):
    """return HBNB"""
    return 'Python ' + text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def python_number(n):
    """Retrun the number"""
    return str(n) + ' is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
