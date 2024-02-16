#!/usr/bin/python3
""" 
starts a Flask web application 
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
	""" hello_hbnb fonction """
	return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
	""" hbnb fonction """
	return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
	""" c_text fonction """
	ftesxt = text.replace('_', ' ')
	return 'C {}'.format(ftesxt)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
	"""" python_text fonction """
	ftesxt = text.replace('_', ' ')
	return 'Python {}'.format(ftesxt)


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
	""" number fonction """
	return '{} is a number'.format(n)


if __name__ == "__main__":
	app.run(host="0.0.0.0")
