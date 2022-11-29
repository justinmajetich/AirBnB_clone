#!/usr/bin/python3
"""
Displays the states lists
"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Lists all the states with the storage.all() method"""
    states = storage.all("State")
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(exit):
    """Closes the database when the session ends"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
