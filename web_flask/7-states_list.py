#!/usr/bin/python3
"""
List of States
"""
from models import storage
from flask import Flask, render_template
from models.state import State
from models import *
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def state_list():
    """display a HTML page with the states listed in alphabetical order"""
    states_list = sorted(list(storage.all(State)), key = lambda x: x.name)
    return render_template('7-states_list.html', states_list=states_list)

@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
