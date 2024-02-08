#!/usr/bin/python3
'''
Module Docs
'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Method Docs'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Method Docs'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    '''Method Docs'''
    text = text.replace('_', ' ')
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
