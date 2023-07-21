#!/usr/bin/python3
"""
0-hello_route.py: A script that starts a flask web application
"""
from flask import Flask

app = Flask(__name__)

"""Route to display "Hello HBNB!" """


@app.route('/', strict_slashes=False)
def hello():
    """funtion that returns Hello HBNB!"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def helloHBNB():
    """funtion that returns HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def helloC(text):
    """funtion that returns "C <text(i.e a variable)>" """
    """text = escape(text)"""
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
