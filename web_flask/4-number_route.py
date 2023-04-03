#!/usr/bin/python3
"""Flask hello world"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def hello_world():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def C_text(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/python/<text>")
def python_text(text):
    return "Python {}".format(text.replace("_", " "))


@app.route("/python/")
def python_notext():
    return "Python {no_text}".format(no_text="is cool")

@app.route("/number/<int:n>")
def is_number(n):
    return ("{} is a number".format(n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
