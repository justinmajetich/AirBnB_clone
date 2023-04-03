#!/usr/bin/python3
"""
Flask website with a single paragraph
that says "Hello, HBNB!".
"""
from flask import Flask

app = Flask(__name__)

@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    HTML paragraph with "Hello, HBNB!"
    in it.
    """
    return "<p>Hello HBNB!</p>"
