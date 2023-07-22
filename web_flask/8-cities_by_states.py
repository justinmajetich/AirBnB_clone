#!/usr/bin/python3
# File: 8-cities_by_states.py
# Authors: Yoshua Lopez - Ma paz Quirola - Laura Socarras 
# email: 

""""
Script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:
            /cities_by_states:    Display HTML and state, city relations
"""

from models import storage
from models.state import State
from flask import Flask, render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(self):
    """After each request remove current SQLAlchemy session"""
    storage.close()


@app.route("/cities_by_states")
def cities_by_states():
    """Displays an HTML page with a list of all states and related cities.
       States/cities are sorted by name.
    """
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
