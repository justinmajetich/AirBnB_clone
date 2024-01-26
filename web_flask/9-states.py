#!/usr/bin/python3

from flask import Flask, render_template
from models import storage
from models import *
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state(id=None):
    States = storage.all(State)
    if id is not None:
        id = "State.{}".format(id)
    return render_template('9-states.html', states=States, state_id=id)


@app.teardown_appcontext
def tear_db(exception):
    return storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
