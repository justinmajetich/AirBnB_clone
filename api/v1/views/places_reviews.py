#!/usr/bin/python3
""" objects that handle all default RestFul API actions for Reviews """
from models.review import Review
from models.place import Place
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from


@app_views.route('/places/<place_id>/reviews', methods=['GET'],
                 strict_slashes=False)
@swag_from('documentation/reviews/get_reviews.yml', methods=['GET'])
def get_reviews(place_id):
    """
    Retrieves the list of all Review objects of a Place
    """
    place = storage.get(Place, place_id)

    if not place:
        abort(404)

    reviews = [review.to_dict() for review in place.reviews]

    return jsonify(reviews)


@app_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/reviews/get_review.yml', methods=['GET'])
def get_review(review_id):
    """
    Retrieves a Review object
    """
    review = storage.get(Review, review_id)
    if not review:
        abort(404)

    return jsonify(review.to_dict())


@app_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
@swag_from('documentation/reviews/delete_reviews.yml', methods=['DELETE'])
def delete_review(review_id):
    """
    Deletes a Review Object
    """

    review = storage.get(Review, review_id)

    if not review:
        abort(404)

    storage.delete(review)
    storage.save()

    return make_response(jsonify({}), 200)


@app_views.route('/places/<place_id>/reviews', methods=['POST'],
                 strict_slashes=False)
@swag_from('documentation/reviews/post_reviews.yml', methods=['POST'])
def post_review(place_id):
    """
    Creates a Review
    """
    place = storage.get(Place, place_id)

    if not place:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'user_id' not in request.get_json():
        abort(400, description="Missing user_id")

    data = request.get_json()
    user = storage.get(User, data['user_id'])

    if not user:
        abort(404)

    if 'text' not in request.get_json():
        abort(400, description="Missing text")

    data['place_id'] = place_id
    instance = Review(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)


@app_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/reviews/put_reviews.yml', methods=['PUT'])
def put_review(review_id):
    """
    Updates a Review
    """
    review = storage.get(Review, review_id)

    if not review:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'user_id', 'place_id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(review, key, value)
    storage.save()
    return make_response(jsonify(review.to_dict()), 200)
