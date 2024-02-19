#!/usr/bin/python3
"""a script that starts a flask web"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def index():
    """initials the url"""
    return "Hello HBNB!"

@app.route('/hbnb')
def hbnb():
    """returns HBNB"""
    return "HBNB
