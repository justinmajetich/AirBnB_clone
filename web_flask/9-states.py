#!/usr/bin/python3
"""States and state"""

from flask import Flask, render_template
from models import storage, State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states(id=None):
    """Fetch all states from storage engine"""
    states_dict = storage.all(State)

    if id:
        state_key = states_dict.get(f"State.{id}")
    else:
        state_key = None

    return render_template(
        '9-states.html',
        states=states_dict,
        model_id=id,
        state=state_key
    )


@app.teardown_appcontext
def teardown_appctxt(exception):
    """Remove SQLAlchemy session after each request"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
