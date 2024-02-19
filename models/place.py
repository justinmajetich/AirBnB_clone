#!/usr/bin/python3
"""Place Module for HBNB project"""
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from models import type_of_storage, storage
from models.review import Review


class Place(BaseModel):
    """A place to stay"""

    if type_of_storage == 'db':
        reviews = relationship(
            'Review',
            cascade='all, delete-orphan',
            backref='place'
            )
    else:
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

        @property
        def reviews(self):
            """
            Returns the list of Review instances with place_id
            equal to the current Place.id. It's the FileStorage
            relationship between Place and Review.

            """
            all_reviews = storage.all(Review)
            reviews = []
            for review in all_reviews.values():
                if review.place_id == self.id:
                    reviews.append(review)
            return reviews
