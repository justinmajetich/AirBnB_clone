#!/usr/bin/python3
'''Script that starts a Flask web application'''
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states", strict_slashes=False")
@app.route("/states/<id>", strict_slashes=False)
def states(id='0'):
        return render_template('9-states.html',
                               states=storage.all(State).values())


@app.teardown_appcontext
def close(response_or_ex):
        storage.close()

if __name__ == "__main__":
        app.run(debug=True)
