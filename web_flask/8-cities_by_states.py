#!/usr/bin/python3
"""A script that lists cities by states"""
from flask import Flask, render_template
from models import storage
from models import State
from operator import attrgetter


app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Displays an HTML page"""
    states = storage.all(State).values()
    s_sorted = sorted(states, key=attrgetter('name'))
    return render_template('8-cities_by_states.html', States=s_sorted)


@app.teardown_appcontext
def teardown_app_context(exception):
    """It removes the current SQLAlchemy sessions after each requests"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
