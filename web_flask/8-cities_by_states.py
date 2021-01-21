#!/usr/bin/python3
'''Script that starts a Flask web application'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
        return render_template('8-cities_by_states.html',
                               states=storage.all(State).value())


@app.teardown_appcontext
def close(response_or_ex):
        storage.close()

if __name__ == "__main__":
        app.run(debug=True)
