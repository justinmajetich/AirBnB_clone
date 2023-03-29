#!/usr/bin/python3
"""Script that starts a Flask web application"""
from models import storage
from flask import render_template, Flask
app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    """Cities by states"""
    states = storage.all('State')
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Remove current SQLALchemy sesh"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
