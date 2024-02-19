#!/usr/bin/python3
"""8-cities_by_states module
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/cities_by_states")
def cities_by_states():
    """Displays HTML page
    H1 tag: States
    UL tag: list of all State objects in DBStorage sorted by name
    LI tag: list of City objects linked to State sorted by name
    """
    return render_template("8-cities_by_states.html",
                           data=storage.all(State).values())


@app.teardown_appcontext
def storage_close(var=None):
    """Removes current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
