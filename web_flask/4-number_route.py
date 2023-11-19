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


@app.route('/c/<text>', strict_slashes=False)
def ello_puppet(text):
    """Returns this string"""
    processed_text = text.replace('_', ' ')
    return f"C {processed_text}"


@app.route('/python/', defaults={'text': 'is_cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def ello_python(text):
    """Returns this string"""
    processed_text = text.replace('_', ' ')
    return f"Python {processed_text}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Returns if n is an integer """
    return f"{n} is a number"


""" Setting the localhost and port """
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
