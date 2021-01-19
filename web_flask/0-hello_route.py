#!/usr/bin/python3
'''Script that starts a Flask web application'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB!"

