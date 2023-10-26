#!/usr/bin/python3
"""Flask package"""

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    """hello world testing"""
    return 'Hello, World!'
