#!/usr/bin/python3
"""Simple Flask Module instance"""
from flask import Flask, render_template

app = Flask(__name__, template_folder="../templates/")


@app.route("/", strict_slashes=False)
def hello():
    """Simple route to return a string"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Simple route to return a string"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """C Followed by the variable value"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """Python route with default text variable value"""
    text = text.replace("_", " ")
    return f"Python {text}"


@app.route("/number/<int:n>", strict_slashes=False)
def number_n(n):
    """Displays the number if n is an integer"""
    return f"{n} is a number"


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display a HTML page only if n is an interger"""
    return render_template("5-number.html", n=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
