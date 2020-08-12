#!/usr/bin/python3
""" Place Module for HBNB project """

from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, Float, String, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

place_amenity = Table(
    'place_amenity',
    Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id')),
    Column('amenity_id', String(60), ForeignKey('amenities.id'))
)


class Place(BaseModel, Base):
    """ A place to stay """

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024), nullable=True)
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float, nullable=True)
        longitude = Column(Float, nullable=True)
        amenity_ids = []

        reviews = relationship(
            "Review",
            backref="place",
            cascade="all, delete-orphan"
        )

        amenities = relationship(
            "Amenity",
            secondary=place_amenity,
            viewonly=False
        )
    else:
        from models import storage

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
            """return the reviews linked with the place"""
            place_review = []
            review_all = storage.all(Review)
            for review in review_all.values():
                if review.place_id == self.id:
                    place_review.append(review)
            return place_review

        @property
        def amenities(self):
            """return the amenities linked with the place"""
            place_amenities = []
            amenities_all = storage.all(Amenity)
            for amenity in amenities_all.values():
                if amenity.id in amenity_ids:
                    place_amenities.append(review)
            return place_amenities

        @amenities.setter
        def amenities(self, amenity):
            """add a new amenity to the place"""
            if type(amenity) is Amenity:
                amenity_ids.append(amenity.id)
