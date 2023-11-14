#!/usr/bin/python3
""" Starts a Flask web app """
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """ Displays list of states from DB """
    storage.reload()
    all_states = storage.all(State)

    states_list = []

    for state in all_states:
        states_list.append(all_states[state])

    return render_template('8-cities_by_states.html', states=states_list)


@app.teardown_appcontext
def teardown(exception):
    """ Closes current SQLAlchemy Sesh """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
