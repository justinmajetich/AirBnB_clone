#!/usr/bin/python3
"""a script that starts a flask web"""
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """initials the url"""
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """returns HBNB"""
    return "HBNB"

@app.route('/c/<text>')
def text():
    """texts"""
    return 'C ' + escape(text).replace('_', ' ')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
