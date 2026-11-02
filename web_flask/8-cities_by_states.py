#!/usr/bin/python3
"""script starts a flask application"""

from flask import Flask, render_template
from models import storage


app = Flask(__name__)
"""flask app"""


@app.teardown_appcontext
def tear_down(self):
    """Method close the db session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """displays the cities by states"""
    states = storage.all('State')
    return render_template('8-cities_by_states.html',
                           states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0')
