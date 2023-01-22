#!/usr/bin/python3
"""API endpoint"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.state import State


@app_views.route('/states')
def all_states():
    """Return list of all states"""
    all_states = storage.all("State").values()
    return jsonify([obj.to_dict() for obj in all_states])


@app_views.route('/states', methods=['POST'])
def add_state():
    """Add state to states"""
    data = request.get_json(silent=True)
    if not data:
        return jsonify({'error': "Not a JSON"}), 400
    name = data.get('name', None)
    if not name:
        return jsonify({'error': "Missing name"}), 400

    # this State already exists. Just update State with new data
    for state in storage.all("State").values():
        if state.name == name:
            setattr(state, "name", name)
            state.save()
            return jsonify(state.to_dict()), 200

    data.pop("id", None)
    data.pop("created_at", None)
    data.pop("updated_at", None)

    state = State(**data)
    state.save()
    return jsonify(state.to_dict()), 201


@app_views.route('/states/<state_id>', methods=['GET', 'PUT', 'DELETE'])
def manipulate_state(state_id):
    """GET/UPDATE/DELETE State object based off id else raise 400"""

    state = storage.get("State", state_id)  # Get State
    if not state:
        abort(404)

    if request.method == 'PUT':  # Update State
        data = request.get_json(silent=True)
        if not data:
            return jsonify({'error': "Not a JSON"}), 400
        # update attributes
        [setattr(state, key, value) for key, value in data.items()
         if key not in ["id", "created_at", "updated_at"]]
        state.save()

    if request.method == 'DELETE':  # Delete State
        state.delete()
        storage.save()
        return jsonify({}), 200  # DELETE method

    return jsonify(state.to_dict()), 200  # GET, PUT method
