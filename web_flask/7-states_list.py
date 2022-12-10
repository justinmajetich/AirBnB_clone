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


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with all States objects from DBStorage

    States are sorted by name
    """
    data = storage.all(State).values()
    return (render_template('7-states_list.html', states=data))


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
