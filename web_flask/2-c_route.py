#!usr/bin/python3
"""Create flask app"""
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    """Home route"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    return "HBNB"


@app.route("/c/<text>")
def c_route(text):
    text = text.replace('_', ' ')
    return f"C {text}"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
