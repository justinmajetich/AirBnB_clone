#!/usr/bin/python3
"""Simple Flask Module instance"""
from flask import Flask, render_template

from models import storage
from models.city import City
from models.state import State

app = Flask(__name__)


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


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def number_odd_or_even(n):
    """Display a HTML only if n is an integer and it's type even|odd"""
    return render_template("6-number_odd_or_even.html", n=n)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Display a HTML page with all State objects present in DBStorage"""
    states = storage.all(State)
#    states = sorted(states.values(), key=lambda state: state.name)
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Display a HTML page with all State and City present in DBStorage"""
    states = storage.all(State)
    states = sorted(states.values(), key=lambda state: state.name)
    cities = storage.all(City)
    return render_template(
            "8-cities_by_states.html",
            states=states
            )


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
