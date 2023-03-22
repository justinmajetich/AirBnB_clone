#!/usr/bin/python3
# starts flask with c thing
from flask import Flask, abort

app = Flask(__name__)


@app.route('/')
def hello_world():
    # hello
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    # hbnb
    return 'HBNB'


@app.route('/c/<text>')
def ctext(text):
    # c with text
    return 'C ' + text.replace("_", ' ')


@app.route('/python/')
@app.route('/python/<text>')
def ptext(text='is cool'):
    # python with text
    return 'Python {}'.format(text.replace("_", ' '))


@app.route('/number/<n>')
def ntext(n):
    # number
    try:
        return '{} is a number'.format(int(n))
    except:
        abort(404)


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
