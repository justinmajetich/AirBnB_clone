#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Flask web application
Created on Tue Sep  1 11:15:54 2020
@author: Robinson Montes
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Start a basic Flask web application"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return the string 'HBNB!'"""
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
