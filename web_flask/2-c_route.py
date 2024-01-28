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


@app.route('/c/<text>')
def text(text):
    '''
    display “C ” followed by the value of the text variable
    '''
    text = text.replace("_", " ")
    return f"C {text}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
