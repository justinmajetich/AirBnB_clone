#!/usr/bin/python3
""" Starts a Flask web that lists states """
from flask import Flask, render_template
from models.state import State
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_list_page(id=None):
    return render_template("9-states.html", bd=storage.all(State), id=id)


@app.teardown_appcontext
def terdown_db(close):
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
