#!/usr/bin/python3
"""Import Modules"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """states_list route, return all states with ID and state"""
    states = storage.all(State)
    return render_template('7-states_list.html', State=states.values())


@app.teardown_appcontext
def teardown_db():
    """Function to close the connection to the database"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
