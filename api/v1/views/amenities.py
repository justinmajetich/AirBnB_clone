#!/usr/bin/python3
"""API endpoint"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity


@app_views.route('/amenities')
def all_amenities():
    """Return list of all amenities"""
    all_amenities = storage.all("Amenity")
    return jsonify([obj.to_dict() for obj in all_amenities.values()])


@app_views.route('/amenities', methods=['POST'])
def add_amenity():
    """Add amenity to states"""
    data = request.get_json(silent=True)
    if not data and data != {}:
        return jsonify({'error': "Not a JSON"}), 400
    name = data.get('name', None)
    if not name:
        return jsonify({'error': "Missing name"}), 400

    data.pop("id", None)
    data.pop("created_at", None)
    data.pop("updated_at", None)

    # this amenity already exists. Just update Amenity with new data
    for amenity in storage.all("Amenity").values():
        if amenity.name == name:
            [setattr(amenity, key, value) for key, value in data.items()]
            amenity.save()
            return jsonify(amenity.to_dict()), 200

    amenity = Amenity(**data)
    amenity.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['GET'])
def get_amenity(amenity_id):
    """GET amenity object based off id"""
    amenity = storage.get("Amenity", amenity_id)
    if not amenity:
        abort(404)
    return jsonify(amenity.to_dict()), 200


@app_views.route('/amenities/<amenity_id>', methods=['PUT'])
def update_amenity(amenity_id):
    """UPDATE amenity object based off id"""
    amenity = storage.get("Amenity", amenity_id)
    if not amenity:
        abort(404)

    data = request.get_json(silent=True)
    if not data:
        return jsonify({'error': "Not a JSON"}), 400
    for key, value in data.items():
        if key in ["id", "created_at", "updated_at"]:
            continue
        setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict()), 200


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'])
def delete_amenity(amenity_id):
    """DELETE amenity object based off id"""
    amenity = storage.get("Amenity", amenity_id)
    if not amenity:
        abort(404)
    amenity.delete()
    storage.save()
    return jsonify({}), 200
