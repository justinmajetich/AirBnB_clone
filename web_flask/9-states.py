#!/usr/bin/python3
# File: 9-states.py
# Authors: Yoshua Lopez - Ma paz Quirola - Laura Socarras
# email: 

""""
Script starts Flask web app
    listen on 0.0.0.0, port 5000
    routes: /:
            /states/<id>:    Display HTML and state, city given state id
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


@app.route('/states')
@app.route('/states/<id>')
def states_and_cities(id=None):
    """Display html page; customize heading with state.name
       fetch sorted cities for this state ID into LI tag ->in HTML file
    """
    states = storage.all(State).values()
    if id is not None:
        for state in states:
            if state.id == id:
                return(render_template("9-states.html", states=state))
        return(render_template("9-states.html"))
    return(render_template("9-states.html", states=states, variable=True))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
