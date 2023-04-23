#!/usr/bin/python3
""" hello route module """
from flask import Flask


app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Displays Hello HBNB!"""
    return 'Hello HBNB!'