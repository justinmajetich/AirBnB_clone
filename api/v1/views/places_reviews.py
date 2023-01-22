#!/usr/bin/python3
"""Review API endpoint"""
from flask import abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.review import Review


@app_views.route("/places/<place_id>/reviews", methods=['GET'])
def get_place_reviews(place_id):
    """Get all reviews associated with a place identified by place_id"""
    place = storage.get("Place", place_id)
    if not place:
        abort(404)
    return jsonify([rev.to_dict() for rev in place.reviews])


@app_views.route("/reviews/<review_id>", methods=['GET'])
def get_review(review_id):
    """Get specific review identified by review_id"""
    review = storage.get("Review", review_id)
    if not review:
        abort(404)
    return jsonify(review.to_dict())


@app_views.route("/reviews/<review_id>", methods=['DELETE'])
def delete_review(review_id):
    """Delete specific review identified by review_id"""
    review = storage.get("Review", review_id)
    if not review:
        abort(404)
    review.delete()
    storage.save()
    return jsonify({})


@app_views.route("/places/<place_id>/reviews", methods=['POST'])
def create_review(place_id):
    """Create new review for place identified by place_id"""
    place = storage.get("Place", place_id)
    if not place:
        abort(404)

    review = request.get_json(silent=True)
    if not review:
        return jsonify(error="Not a JSON"), 400

    if "user_id" not in review:
        return jsonify(error="Missing user_id"), 400

    user = storage.get("User", review["user_id"])
    if not user:
        abort(404)

    if "text" not in review:
        return jsonify(error="Missing text"), 400

    review.pop("id", None)
    review.pop("created_at", None)
    review.pop("updated_at", None)

    review.update({"place_id": place.id, "user_id": user.id})

    review = Review(**review)
    review.save()
    return jsonify(review.to_dict()), 201


@app_views.route("/reviews/<review_id>", methods=['PUT'])
def update_review(review_id):
    """Update existing review identified by review_id"""
    review = storage.get("Review", review_id)
    if not review:
        abort(404)

    updates = request.get_json(silent=True)
    if not updates:
        return jsonify(error="Not a JSON"), 400

    updates.pop("id", None)
    updates.pop("user_id", None)
    updates.pop("place_id", None)
    updates.pop("created_at", None)
    updates.pop("updated_at", None)

    for k, v in updates.items():
        setattr(review, k, v)
    review.save()
    return jsonify(review.to_dict()), 200
