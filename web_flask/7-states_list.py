#!/usr/bin/python3

"""Flask app that lists a list of states
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def teardown_storage(self):
    """Tear down storage after each request"""
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Returns a list of states"""
    states = storage.all(State).values()
    print(states)
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
