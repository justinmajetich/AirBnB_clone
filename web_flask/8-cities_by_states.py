#!/usr/bin/python3
"""
hahahahahahahhahahahahahahaha haha hahahah
"""

from flask import Flask, render_template
from models import storage, State, City

app = = Flask(__name__)


@app.teardown_appcontext
def teardown_seesion(exception):
    """Teardown method to remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Fetch all states(and citites) from the database sorted by name"""
    states = storage.all(State).values()
    sortedStates = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=sortedStates)


if __name__ == '__main__':
    """Main function"""
    app.run(host='0.0.0.0', port=5000)
