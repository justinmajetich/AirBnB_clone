#!/usr/bin/python3
"""starts a Flask web application"""
from models import storage
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def db_teardown(self):
    storage.close()


@app.route('/states', strict_slashes=False)
def states():
    list_states = storage.all('State')
    return render_template('9-states.html', states=list_states)


@app.route('/states/<id>', strict_slashes=False)
def list_city_states(id):
    for state in storage.all('States').values():
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
