#!/usr/bin/python3
""" Set up for Flask app """


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Returns this string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def ello():
    """Returns this string"""
    return "HBNB"


""" Setting the localhost and port """
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
