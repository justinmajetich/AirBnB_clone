#!/usr/bin/python3
"""Import Modules"""
from flask import Flask, render_template
from models import storage
from models.state import State, City
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def method_cities_by_states():
    """route cities by states , prints the state and all its cities"""
    states = storage.all(State)
    return render_template('8-cities_by_states.html', State=states)


@app.teardown_appcontext
def teardown_db(*args, **kwargs):
    """Function to close the connection to the database"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
