#!/usr/bin/python3
"""Script that has 3 routes"""
from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello():
    """Return Hello HBNB"""
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Return HBNB"""
    return "HBNB"

@app.route('/c/<text_param>', strict_slashes=False)
def c_with_text(text_param):
    """Replace underscores with spaces"""
    text = text_param.replace('_', ' ')
    return f"C {text}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
