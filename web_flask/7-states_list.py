#!/usr/bin/python3
"""Script that starts a Flask web application"""
from models import storage
from flask import render_template, Flask
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    states = storage.all('State')
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)