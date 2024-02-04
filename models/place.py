#!/usr/bin/python3
""" Place Module for HBNB project """
import os

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from models.review import Review
from models.amenity import Amenity
import models

place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey("cities.id", ondelete="CASCADE"),
                     nullable=False)
    user_id = Column(String(60), ForeignKey("users.id", ondelete="CASCADE"),
                     nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place")
        amenities = relationship("Amenity", secondary="place_amenity",
                                 viewonly=False,
                                 back_populates="place_amenities")

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """Returns the list of Review instances with place_id equals
            to the current Place.id."""

            reviews = list(models.storage.all(Review).values())

            return list(
                filter(lambda review: (review.place_id == self.id), reviews))

        @property
        def amenities(self):
            """Returns the list of Amenity instances based on
            the attribute amenity_ids that contains all Amenity.id."""

            amenities = list(models.storage.all(Amenity).values())

            return list(
                filter(lambda amenity: (amenity.place_id in self.amenity_ids),
                       amenities))

        @amenities.setter
        def amenities(self, value=None):
            """Adds ids in amenity_ids ."""
            if isinstance(value, type(Amenity)):
                self.amenity_ids.append(value.id)
