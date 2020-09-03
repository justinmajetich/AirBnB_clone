#!/usr/bin/python3
""" States list  """
from flask import Flask
from models import storage
from flask import Flask, render_template
from markupsafe import escape
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def close_storage(arg):
    storage.close()


@app.route('/cities_by_states')
def cities_by_states_route():
    new_dic = storage.all(State)

    return render_template('8-cities_by_states.html', states=new_dic)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
