#!/usr/bin/python3
"""Flask package"""

from flask import Flask, escape, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def get_states_list():
    """Get sttes list"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda k: k.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_down(exception):
    """Relwase Resources"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
