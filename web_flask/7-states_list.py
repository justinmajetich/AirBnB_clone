#!/usr/bin/python3
""" A script that lists states"""
from flask import Flask, render_template
from models import storage
from models import State
from operator import attrgetter
app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display an HTML page"""
    states = [obj for obj in storage.all().values() if isinstance(obj, State)]
    states_sorted = sorted(states, key=attrgetter('name'))
    return render_template('7-states_list.html', States=states_sorted)


@app.teardown_appcontext
def teardown_app_context(exception):
    """It removes the current SQLAlchemy sessions after each requests"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
