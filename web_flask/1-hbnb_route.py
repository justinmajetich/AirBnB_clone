#!/usr/bin/python3
"""create simple flask app"""
from flask import Flask


app = Flask(__name__)

@app.route('/')
def home():
    """Home route """
    return 'Hello HBNB!'

@app.route('/hbnb')
def hbnb():
    """hbnb route"""
    return 'HBNB'

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
