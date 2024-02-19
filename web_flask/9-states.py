#!/usr/bin/python3
"""8-cities_by_states module
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
def states():
    """Displays HTML page
    H1 tag: States
    UL tag: List of all State objects in DBStorage sorted by name
    LI tag: Description of one State: <state.id>: <B><state.name></B>
    """
    return render_template("9-states.html",
                           data=storage.all(State).values())


@app.route("/states/<id>")
def states_id(id=None):
    """Displays HTML page
    H1 tag: States
    H3 tag: Cities
    UL tag: List of City objects linked to the State sorted by name
    LI tag: Description of one City: <city.id>: <B><city.name></B>
    Otherwise: H1 tag: Not found!
    """
    return render_template("9-states.html",
                           data=storage.all(State).values(),
                           id=id)


@app.teardown_appcontext
def storage_close(var=None):
    """Removes current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
