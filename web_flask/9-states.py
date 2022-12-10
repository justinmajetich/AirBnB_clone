#!/usr/bin/python3
"""Script that starts a Flask web application:

Web application must be listening on 0.0.0.0, port 5000
Routes:
    /states_list: display HTML page
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states_list():
    """Displays an HTML page with all States objects from DBStorage

    States are sorted by name
    """
    data = storage.all(State).values()
    return (render_template('7-states_list.html', states=data))


@app.route("/states/<id>", strict_slashes=False)
def states_by_id(id):
    """Displays an HTML page with all the Cities of the State.

    State is searched by id
    Cities are sorted by name
    """
    states = storage.all(State).values()
    state = None
    for st in states:
        if id == st.id:
            state = st
            break
    return (render_template('9-states.html', state=state))


@app.teardown_appcontext
def close_current_session(exception):
    """Close the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
