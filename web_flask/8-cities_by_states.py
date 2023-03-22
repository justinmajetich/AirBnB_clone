#!/usr/bin/python3

"""This module starts a Flask web application to display States and their Cities."""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/cities_by_states', strict_slashes=False)
def cities_route():
    """Renders a template to display all states and their cities."""
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)

@app.teardown_appcontext
def teardown_appcontext(exception):
    """Removes the current SQLAlchemy Session."""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
