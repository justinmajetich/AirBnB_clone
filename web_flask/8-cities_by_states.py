#!/usr/bin/python3
""" Starts a Flask web app """
from flask import Flask, render_template
from models.city import City
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_by_states():
    """ Displays list of states from DB """
    from models import storage
    all_states = storage.all(State)
    list_cities = []

    for x in all_states:
        list_cities.append(all_states[x])

    return render_template('8-cities_by_states.html', states=list_states)


@app.teardown_appcontext
def teardown(close):
    """ Closes current SQLAlchemy Sesh """
    from models import storage
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
