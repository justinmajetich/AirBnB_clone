#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


#!/usr/bin/python3
"""Start a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """Display Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Display HBNB"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Display C followed by text"""
    return "C {}".format(text.replace("_", " "))


@app.route("/python", defaults={"text": "is cool"}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """Display Python followed by text"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Display n is a number only if n is an integer"""
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """Display HTML page only if n is an integer"""
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Display HTML page only if n is an integer"""
    odd_even = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n,
                           odd_even=odd_even)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display HTML page with list of states"""
    states = storage.all("State")
    return render_template("7-states_list.html", states=states)

@app.teardown_appcontext
def teardown_db(exception):
    """Close storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
