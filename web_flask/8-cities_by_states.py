#!/usr/bin/python3
"""Start a Flask web application"""
from models import storage
from models.state import State
from models.city import City
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Close the storage engine"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def display_states():
    """Display a HTML page"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
