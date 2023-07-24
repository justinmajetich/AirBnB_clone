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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):

    # Replace _ with a space
    rep_text = text.replace('_', ' ')
    return ("C {}".format(rep_text))


if __name__ == '__main__':
    app.run()
