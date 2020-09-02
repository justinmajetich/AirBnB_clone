#!/usr/bin/python3
""" script that starts a Flask web application  """
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_route():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb_route():
    return 'HBNB'


@app.route('/c/<text>')
def c_route(text):
    text = text.replace('_', ' ')
    return 'C %s' % escape(text)


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>')
def python_route(text):
    text = text.replace('_', ' ')
    return 'python %s' % escape(text)


@app.route('/number/<int:n>')
def number_route(n):
    return '%s is a number' % escape(n)


@app.route('/number_template/<int:n>')
def number_template_route(n):
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
