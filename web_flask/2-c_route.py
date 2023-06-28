#!/usr/bin/python3
"""
    a script that starts a Flask web application
    and adds several routes for navigation.
"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello_hbnb():
    """ Displays Hello HBNB! """
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """ Displays  HBNB! """
    return "HBNB"


@app.route("/c/<text>")
def hbnb():
    """Displays C followed by
       the value of text 
    """
    return


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
