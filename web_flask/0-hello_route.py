#!/usr/bin/python3
""" script that starts a Flask web application"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    "You must use the option strict_slashes=False in your route definition"""
    return 'Hello HBNB!'
app.run()
