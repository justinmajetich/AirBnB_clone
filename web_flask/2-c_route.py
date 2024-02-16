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

if __name__ == "__main__":
	app.run(host="0.0.0.0")
