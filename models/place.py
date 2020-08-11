#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from models.reviews import Review
from model import storage


class Place(BaseModel):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
    reviews = relationship(
        "Review",
        backref="place",
        cascade="all, delete-orphan"
    )

    def reviews(self):
        state_review = []
        review_all = storage.all(Review)
        for review in review_all.values():
            if review.state_id == self.id:
                state_review.append(review)
        return state_review
