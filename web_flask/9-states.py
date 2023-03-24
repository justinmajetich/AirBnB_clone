#!/usr/bin/python3
"""
Starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exception):
    """Removes the current SQLAlchemy Session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects"""
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_cities(id):
    """Displays an HTML page with a list of all City objects
    linked to a State with a specified id"""
    state = storage.get(State, id)
    if state is None:
        return render_template('7-not_found.html')
    cities = sorted(state.cities, key=lambda x: x.name)
    return render_template('7-states_cities.html', state=state, cities=cities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
