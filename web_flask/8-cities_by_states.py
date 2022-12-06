#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)


@app.teardown_appcontext
def teardown_session(exception):
    """ Teardown """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_html():
    """ Function called with /states_list route """
    states = storage.all(State)
    return render_template('8-cities_by_states.html',
                           Table="States",
                           states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
