#!/usr/bin/python3
"""
Script that starts a Flask web application.
"""
from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states")
@app.route("/states/<id>")
def show_state(id=None):
    """
    Displays an HTML page listing all `city`s inside
    of `state`, sorted by `name`.
    """
    return render_template('9-states.html', states=storage.all(State),
                           id=id)


@app.teardown_appcontext
def teardown(content):
    """
    Removes current SQLAlchemy Session.
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
