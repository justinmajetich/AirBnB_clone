#!/usr/bin/python3
"""
Script that starts a Flask web application
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """
    Display a HTML page with the list of all State objects
    """
    states = storage.all(State)
    return render_template('9-states.html', states=states_sorted)


@app.route('/states/<id>', strict_slashes=False)
def states_cities(id):
    """
    Display a HTML page with the list of City objects linked to a State
    """
     for state in storage.all("State").values():
        if state.id == id: 
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")

@app.teardown_appcontext
def close_session(exception):
    """ 
    Remove the current SQLAlchemy Session after each request
    """
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0')
