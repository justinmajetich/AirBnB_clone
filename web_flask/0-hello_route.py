#!/usr/bin/python3
"""Starts Flask web app
"""
from flask import Flask

app = Flask(__name__)

# Define the route for the root URL '/'
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Displays 'Hello HBNB!'"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
