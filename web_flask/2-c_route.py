#!/usr/bin/python3
""" a script that starts a Flask web application """


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """displays HELLO_HBNB"""
    return "HELLO_HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ displays HBNB in route /hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def C_is_fun(text):
    """ removes underscores from text """
    return "C " + text.replace("_", " ")


if __name__ == "__main__":
    """starts flask server """
    app.run(host='0.0.0.0', port=5000)
