#!/usr/bin/python3
"""User API endpoint"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.user import User


@app_views.route("/users", methods=['GET'])
def all_users():
    """Return list of all users"""
    users = storage.all("User")
    return jsonify([user.to_dict() for user in users.values()]), 200


@app_views.route("/users/<user_id>", methods=['GET'])
def get_user(user_id):
    """Get single user based on user_id, or 404 if not found"""
    user = storage.get("User", user_id)
    if not user:
        abort(404)
    return jsonify(user.to_dict()), 200


@app_views.route("/users/<user_id>", methods=['DELETE'])
def delete_user(user_id):
    """Delete individual user based on user_id, or 404 if not found"""
    user = storage.get("User", user_id)
    if not user:
        abort(404)
    user.delete()
    storage.save()
    return jsonify({}), 200


@app_views.route("/users", methods=['POST'])
def create_user():
    """Create new user from request JSON"""
    user = request.get_json(silent=True)
    if not user:
        return jsonify(error="Not a JSON"), 400
    if "email" not in user:
        return jsonify(error="Missing email"), 400
    if "password" not in user:
        return jsonify(error="Missing password"), 400
    user.pop("id", None)
    user.pop("created_at", None)
    user.pop("updated_at", None)
    user = User(**user)
    user.save()
    return jsonify(user.to_dict()), 201


@app_views.route("/users/<user_id>", methods=['PUT'])
def update_user(user_id):
    """Update existing user based on user_id, or 404 if not found"""
    user = storage.get("User", user_id)
    if not user:
        abort(404)
    updates = request.get_json(silent=True)
    if not updates:
        return jsonify(error="Not a JSON"), 400
    updates.pop("id", None)
    updates.pop("email", None)
    updates.pop("created_at", None)
    updates.pop("updated_at", None)
    for k, v in updates.items():
        setattr(user, k, v)
    user.save()
    return jsonify(user.to_dict()), 200
