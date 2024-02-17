#!/usr/bin/python3
""" Starts a new Flask web application. """

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns the text Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """" Returns the text HBNB """
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
