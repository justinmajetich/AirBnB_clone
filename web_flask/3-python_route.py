#!/usr/bin/python3
"""Import Modules"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_route():
    """Main Route"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb Route"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """c route , return text with spaces"""
    text_with_spaces = text.replace('_', ' ')
    return f"C {text_with_spaces}"


@app.route('/python', defaults={'text': 'is_cool'})
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    """python route, return text with spaces"""
    return "Python {}".format(text.replace('_', ' '))


"""Entry Point"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
