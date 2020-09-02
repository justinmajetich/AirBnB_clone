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


@app.route('/states_list')
def states_list_route():
    new_list = []
    new_dic = storage.all(State)

    for value in new_dic.values():
        new_list.append(value)

    return render_template('7-states_list.html', states=new_list)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
