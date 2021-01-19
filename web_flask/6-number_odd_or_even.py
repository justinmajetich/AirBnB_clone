#!/usr/bin/python3
'''script that starts a Flask web application'''
from flask import Flask, render_template
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


@app.route("/python", defaults={'text': "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    replace = "Python {}".format(escape(text))
    replace1 = replace.replace("_", " ")
    return replace1


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return "{} is a number".format(escape(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    num = n % 2
    return render_template("6-number_odd_or_even.html", n=n, num=num)

if __name__ == "__main__":
    app.run(debug=True)
