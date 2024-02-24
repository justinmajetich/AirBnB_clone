#!/usr/bin/python3
""" Starts a Flask web application """
from flask import Flask, render_template
from models import storage
import models


app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ Display a HTML page """
    states = storage.all(models.State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ Remove the current SQLAlchemy Session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
