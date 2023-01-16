#!/usr/bin/python3
"""
List of States
"""
from models import storage
from flask import Flask, render_template
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    if storage is not None:
        storage.close()


@app.route('/state_list', strict_slashes=False)
def state_list(state_list):
    data = storage.all(State)
    return render_template('7-states_list.html', state_list=data.values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
