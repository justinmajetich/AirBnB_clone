#!/usr/bin/python3
# Set up for Flask app
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
# Using the strict_slashes set to False so that w/out '/' it wont work
def hello():
    return "Hello HBNB!"


""" Setting the localhost and port"""
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
