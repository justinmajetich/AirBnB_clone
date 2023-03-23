#!/usr/bin/Python3
""" This script starts a web flask application"""

from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c(text):
    return f'C {text.replace("_", " ")}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

