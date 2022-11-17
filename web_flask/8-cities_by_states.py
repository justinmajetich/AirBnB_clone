#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def show_states_cities():
    """
    Displays an HTML page listing all `State` objects
    present in `DBStorage` sorted by `name`.
    """
    return render_template('8-cities_by_states.html',
                           states=storage.all(State))


@app.teardown_appcontext
def teardown(content):
    """
    Removes current SQLAlchemy Session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
