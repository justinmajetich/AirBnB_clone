#!/usr/bin/python3
"""
    A script that starts a Flask web application listening
    on 0.0.0.0, port 5000 with Routes [/]: display “Hello HBNB!”
    and [/hbnb]: display “HBNB”
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """ [/]: display “Hello HBNB!” """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """ [/hbnb]: display “HBNB” """
    return "HBNB"


if __name__ == '__main__':
    """ Run module only then ran """
    app.run(host='0.0.0.0', port=5000)
