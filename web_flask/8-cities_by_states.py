#!/usr/bin/python3
"""Script that starts a Flask web application:

Web application must be listening on 0.0.0.0, port 5000
Routes:
    /cities_by_states: display HTML page
"""
from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Displays an HTML page with all States objects with his
    respective Cities. All from DBStorage.

    States and Cities are sorted by name
    """
    data = storage.all(State).values()
    return (render_template('8-cities_by_states.html', states=data))


@app.teardown_appcontext
def teardown_session(exception):
    """Remove the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
