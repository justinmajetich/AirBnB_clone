#!/usr/bin/python3
"""
Flask web application
"""
from flask import Flask, render_template, g
from models import storage
from models.state import State


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Displays a list of all the states and their cities."""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
