#!usr/bin/python3
""""starts a Flask web application:
application must be listening on 0.0.0.0, port 5000
"""
from email.mime import application
from models import storage
from flask import Flask, render_templete

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display a HTML page"""
    states = storage.all("State")
    return render_templete('7-states_list.html', states=states)


@app.teardown_appcontext:
    def teardown(exc):
        """remove the current SQLAlchemy Session"""
        storage.close()

if __name__ == '__main__':
    app.run(host="0.0.0.0")
