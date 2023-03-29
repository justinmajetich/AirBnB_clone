#!/usr/bin/python3
"""Script that starts a Flask web application"""
from models import storage
from flask import render_template, Flask
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Holds states"""
    states = storage.all("State")
    return render_template("9-states.html", state=states)


@app.route("/states/<id>", strict_slashes=False)
def states_id(id):
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


@app.teardown_appcontext
def teardown(exc):
    """Remove current SQLALchemy sesh"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
