#!/usr/bin/python3
"""7-states_list module
Starts a Flask web application
"""

from flask import Flask, render_template
from models import storage, State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states_list")
def state_list():
    """Displays HTML page
    H1 tag: States
    UL tag: list of all State objects in DBStorage sorted by name
    """
    return render_template("7-states_list.html",
                           data=storage.all(State).values())


@app.teardown_appcontext
def storage_close(var=None):
    """Removes current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
