#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base, Relationship
import models
from sqlalchemy import (
    Column,
    Integer,
    String,
    FLOAT,
    ForeignKey
)


class Place(BaseModel, Base):
    """ A place to stay """
    if models.storage_type == "db":
        __tablename__ = "places"
        city_id = Column(String(128), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(128), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(128), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(FLOAT(precision=10), nullable=True)
        longitude = Column(FLOAT(precision=10), nullable=True)
        # amenity_ids = "I no sabi weytin i go use dis one do"
        reviews = Relationship(
            "Review", cascade="all, delete", backref="place")
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
        Returns the list of Review instances with
        place_id equals to the current Place.id
        """

        from models import storage

        my_reviews = []
        all_reviews = storage.all('Reviews')
        for review in all_reviews.values():
            if review.place_id == self.id:
                my_reviews.append(review)
        return my_reviews
