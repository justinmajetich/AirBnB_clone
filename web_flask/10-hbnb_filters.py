#!/usr/bin/python3
""" States and State  """
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


@app.route('/states/', defaults={'id': None})
@app.route('/states/<id>')
def states_list_route(id):
    states_dic = storage.all(State).values()

    if (id is None):
        return render_template('9-states.html', states=states_dic)

    state_status = False
    for state in states_dic:
        if state.id == id:
            state_status = True
            break

    if (state_status):
        return render_template('9-states.html', state=state)

    return render_template('9-states.html')

@app.route('/hbnb_filters/')
def list_filters():
    return render_template('10-hbnb_filters.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
