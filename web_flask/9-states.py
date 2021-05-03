#!/usr/bin/python3
"""starts a Flask web application listening on 0.0.0.0, port 5000"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """remove the current sqlalchemy session"""
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    """list all states"""
    states = storage.all('State')
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_by_id(id):
    """Display the matched state and its cities"""
    states = storage.all('State').values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', states=state)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
