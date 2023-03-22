#!/usr/bin/python3
# starts flask with c thing
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    # prints hello
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    # prints hbnb
    return 'HBNB'


@app.route('/c/<text>')
def ctext(text):
    # prints c with input
    return 'C ' + text.replace("_", ' ')


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
