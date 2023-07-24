#!/usr/bin/python3
""" Script that starts a Flask web app on :500 """
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hi_hbnb():
    return 'HBNB'


if __name__ == '__main__':
    app.run()
