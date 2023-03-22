#!/usr/bin/python3
# list of states
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route('/states_list')
def stateList():
    # lists states in html
    return render_template('8-cities_by_states.html',
                           storage=storage.all('State'))


@app.route('/cities_by_states')
def cityStateList():
    # lists states in html
    return render_template('8-cities_by_states.html',
                           storage=storage.all('State'))


@app.teardown_appcontext
def closer(exception):
    storage.close()


if __name__ == "__main__":
    app.url_map.strict_slashes = False
    app.run(host="0.0.0.0", port=5000)
