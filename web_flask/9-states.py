#!/usr/bin/python3
"""
Flask application to display states and their cities.
"""
from models import storage
from flask import render_template, Flask

app = Flask(__name__)

@app.route("/states", strict_slashes=False)
def states():
    """
    Display a list of all State objects sorted by name.
    """
    states = storage.all("State")
    return render_template("9-states.html", states=states)

@app.route("/states/<id>", strict_slashes=False)
def state_detail(id):
    """
    Display details of a specific State object and its cities.
    """
    for state in storage.all("State").values():
        if state.id == id:
            # Assuming state.cities is a list of City objects
            return render_template("state_detail.html", state=state, cities=state.cities)
    return render_template("not_found.html")

@app.teardown_appcontext
def teardown(exc):
    """
    Close the storage session after each request.
    """
    storage.close()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
