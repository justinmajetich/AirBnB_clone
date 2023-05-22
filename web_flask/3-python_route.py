#!/usr/bin/python3
"""A script that starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_flask():
    """Display a string when route is queried
    """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Display a string when route queried
    """
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    """Display “C ” followed by the value of the text variable,
       replace underscore symbols with a space
    """
    return 'C ' + text.replace('_', ' ')


@app.route('/python/')
@app.route('/python/<text>')
def python_with_text(text='is cool'):
    """Display “Python ”, followed by the value of the text variable,
       replace underscore symbols with a space
    """
    return 'Python ' + text.replace('_', ' ')


if __name__ == '__main__':
    app.url_map.strict_slashes = False
    app.run(host='0.0.0.0', port=5000)
