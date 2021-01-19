#!/usr/bin/python3
'''
Script that starts a Flask web application
'''
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    return 'Hello HBNB!'
