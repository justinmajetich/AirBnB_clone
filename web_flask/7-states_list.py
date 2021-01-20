#!/usr/bin/python3
""" Start Flask Web Application """
from flask import Flask
from flask import render_template
from models import storage
app = Flask(__name__)


@app.teardown_appcontext
def close_session(self)
    """ close storage """
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list_route():
    """ varible sends a numeric in HTML """
    return render_template("7-states_list.html", states=storage.all('State'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port="5000")
