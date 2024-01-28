#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Displays Hello HBNB!
    """
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Displays HBNB!
    """
    return ('HBNB')


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    '''
    display “C ” followed by the value of the text variable
    '''
    text = text.replace("_", " ")
    return f"C {text}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    """
     display “Python ”, followed by the value of the text variable
    """
    return f'Python {text.replace("_", " ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def python_N(n):
    """
     display “n is a number” only if n is an integer
    """
    if isinstance(n, int):
        return f'{n} is a number'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
