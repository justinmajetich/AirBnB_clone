#!/usr/bin/python3
""" Starts a Flask web app """


from flask import Flask, render_template, g
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Displays list of states from DB """
    states = sorted(list(storage.all(State).values()), key=lambda x: x.name)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(error=None):
    """ Closes current SQLAlchemy Sesh """
    current_storage = getattr(g, "storage", None)
    if current_storage is not None:
        current_storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
