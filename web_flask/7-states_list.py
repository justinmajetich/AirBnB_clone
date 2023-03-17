#!/usr/bin/python3
from flask import Flask
from models import storage, State
from flask import render_template

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exceptions):
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    state_obj = storage.all("State")
    states = list()
    for state, value in state_obj.items():
        states.append(value)
    return render_template("7-states_list.html", states=states)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
