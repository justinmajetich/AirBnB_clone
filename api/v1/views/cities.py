#!/usr/bin/python3
"""City API endpoint"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.city import City


@app_views.route('/states/<state_id>/cities')
def all_cities(state_id):
    """Return list of all cities associated with a particular state"""
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    return jsonify([city.to_dict() for city in state.cities]), 200


@app_views.route('/cities/<city_id>', methods=['GET'])
def city_by_id(city_id):
    """Return City object based off id else raise 404"""
    city = storage.get("City", city_id)
    if not city:
        abort(404)
    return jsonify(city.to_dict()), 200


@app_views.route('/cities/<city_id>', methods=['DELETE'])
def delete_city(city_id):
    """Return City object based off id else raise 404"""
    city = storage.get("City", city_id)
    if not city:
        abort(404)
    city.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route('/states/<state_id>/cities', methods=['POST'])
def create_city(state_id):
    """Create new City object from request JSON else raise 400"""
    city = request.get_json(silent=True)
    if not city:
        return jsonify({"error": "Not a JSON"}), 400
    if 'name' not in city:
        return jsonify({"error": "Missing name"}), 400
    state = storage.get("State", state_id)
    if not state:
        abort(404)
    city.pop("state_id", None)
    city.pop("id", None)
    city.pop("created_at", None)
    city.pop("updated_at", None)
    city_exists = list(filter(lambda c: c.name == city["name"], state.cities))
    if city_exists:
        for k, v in city.items():
            setattr(city_exists[0], k, v)
        city_exists[0].save()
        return jsonify(city_exists[0].to_dict()), 200
    city = City(state_id=state_id, **city)
    city.save()
    return jsonify(city.to_dict()), 201


@app_views.route('/cities/<city_id>', methods=['PUT'])
def update_city(city_id):
    """Update City object using data from JSON request else raise 400"""
    city = storage.get("City", city_id)
    if not city:
        abort(404)
    updates = request.get_json(silent=True)
    if not updates:
        return jsonify({"error": "Not a JSON"}), 400
    updates.pop("id", None)
    updates.pop("created_at", None)
    updates.pop("updated_at", None)
    updates.pop("state_id", None)
    for k, v in updates.items():
        setattr(city, k, v)
    city.save()
    return jsonify(city.to_dict()), 200
