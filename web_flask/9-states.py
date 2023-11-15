#!/usr/bin/python3
"""Script that starts a flask web application"""
from flask import Flask
from flask import render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states_list():
    return render_template('9-states.html',
                           states=storage.all(State))


@app.route('/states/<id>', strict_slashes=False)
def state_id_list(id):
    state_list = storage.all(State)
    state = state_list.get(id)
    return render_template('9-states.html', state=state)


@app.teardown_appcontext
def teardown(exception):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
