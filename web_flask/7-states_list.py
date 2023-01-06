#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def handle_teardow(self):
    """
    Después de cada solicitud, debe eliminar
    la sesión actual de SQLAlchemy
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def list_of_state():
    """
    Función llamada con la ruta /states_list
    """
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
