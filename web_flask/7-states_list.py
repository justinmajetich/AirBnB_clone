#!/usr/bin/python3
"""
Starts a Flask web application
"""


from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ removes current SQLAlchemy Session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ displays 7-states_list.html """
    states = storage.all("State").values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
