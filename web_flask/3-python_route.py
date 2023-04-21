#!/usr/bin/python3
"""
/python/(<text>): display “Python ”, followed by the value of the text
variable (replace underscore _ symbols with a space )
The default value of text is “is cool” and double route
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    return 'HBNB'


@app.route('/c/<c_variable>', strict_slashes=False)
def cisfun(c_variable):
    return 'C {}'.format(c_variable.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<python_variable>', strict_slashes=False)
def pythoniscool(python_variable='is_cool'):
    return 'Python {}'.format(python_variable.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
