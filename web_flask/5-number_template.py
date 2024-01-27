#!/usr/bin/python3
"""starts a Flask web application"""


from flask import Flask
from flask import render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/", strict_slashes=False)
def hello_world():
    """ Returns some text. """
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def disp_hbnb():
    """display HBNB"""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """Display  c follwed by the value text"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """display Python, followed by the value of the text """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>')
def number_root(n):
    """display n is a number only if n is an integer"""
    n = str(n)
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def n_html(n):
    """display html page only if n is an int"""
    n = str(n)
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
