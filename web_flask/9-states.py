#!/usr/bin/python3
"""
flask model
"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
storage.all()


@app.teardown_appcontext
def teardown_data(self):
    """
        refresh data
    """
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_id(id=None):
    """
        list state by id if found
    """
    info = []
    states = storage.all(State)
    if id is None:
        for k in states:
            info.append(states[k])
    else:
        id = 'State.' + id
        info = states.get(id)
    return render_template('9-states.html', states=info, id=id)
    return render_template('9-states.html', state=id)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
