#!/usr/bin/python3
"""a script that starts a Flask web app display is a number only if n is an integer"""

from flask import Flask, escape

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route handler for the root URL ('/').

    Returns:
        str: A simple greeting message.
    """
    return "Hello HBNB!"

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route handler for the '/hbnb' URL.

    Returns:
        str: The string "HBNB".
    """
    return "HBNB"

@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    Route handler for the '/c/<text>' URL.

    Args:
        text (str): The text provided in the URL.

    Returns:
        str: The string "C " followed by the value of the text variable.
    """
    return "C {}".format(escape(text.replace("_", " ")))

@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """
    Route handler for the '/python/' URL with a default value and '/python/<text>' URL.

    Args:
        text (str): The text provided in the URL.

    Returns:
        str: The string "Python " followed by the value of the text variable.
    """
    return "Python {}".format(escape(text.replace("_", " ")))

@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    Route handler for the '/number/<n>' URL with a number parameter.

    Args:
        n (int): The numeric value provided in the URL.

    Returns:
        str: The string "{n} is a number" if n is an integer, else a 404 Not Found error.
    """
    return f"{n} is a number"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
