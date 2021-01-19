#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    return "Hello HBNB"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    replace = "C {}".format(escape(text))
    replace1 = replace.replace("_", " ")
    return replace1

if __name__ == "__main__":
    app.run(debug=True)
