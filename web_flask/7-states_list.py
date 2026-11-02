#!/usr/bin/python3
"""script starts a flask application"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)
"""flask app"""


@app.route('/states_list', strict_slashes=False)
def get_list():
    """displays a list of all states"""
    states = storage.all('State')
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_down(exception):
    """Method close the db session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0')
