#!/usr/bin/python3
""" script that starts a Flask web application  """
from flask import Flask
from markupsafe import escape


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    return 'HBNB'


@app.route('/c/<text>')
def c_is_fun(text):
    text = text.replace('_', ' ')
    return 'C %s' % escape(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
