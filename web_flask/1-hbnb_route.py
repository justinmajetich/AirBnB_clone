#!/usr/bin/python3
'''Script that starts a Flask web application'''
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"

if __name__ == "__main__":
    app.run(debug=True)