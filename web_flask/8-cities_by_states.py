#!/usr/bin/python3
"""Flask hello world"""

from flask import Flask, render_template
from models import storage
from models.state import State

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


@app.route("/number_template/<int:n>")
def is_number_template(n):
    return render_template("5-number.html", n=n)


@app.route("/number_odd_or_even/<int:n>")
def odd_or_even(n):
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", n=n, parity='even')
    else:
        return render_template("6-number_odd_or_even.html", n=n, parity='odd')


@app.teardown_appcontext
def teardown_db(exception):
    """Removes SQLAlchemy session"""
    storage.close()


@app.route("/states_list")
def states_list():
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.route("/cities_by_states")
def cities_by_states():
    states = list(storage.all(State).values())
    states.sort(key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
