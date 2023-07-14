#!/usr/bin/python3
"""
script that starts a Flask web application
"""
from flask import Flask

app = Flask(__name__)

def hello_world():
    return 'Hello, World!'

app.run()