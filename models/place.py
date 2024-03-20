#!/usr/bin/python3
""" Place Module for HBNB project """

from os import getenv
from sqlalchemy.orm import relationship
from sqlalchemy import Table, Float, Column, String, Integer, ForeignKey
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models.review import Review
import models


class Place(BaseModel, Base):
    """A place to stay"""

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

    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship(
            "Review", backref="place", cascade="all, delete, delete-orphan"
        )
        amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=False,
            back_populates="place_amenities",
        )
    else:

        @property
        def reviews(self):
            """Returns a list of review instances"""
            review_list = []
            for review in models.storage.all(Review).values():
                if review.place_id == self.id:
                    review_list.append(review)
            return review_list

        @property
        def amenities(self):
            """Returns a list of amenity instances"""
            amenity_list = []
            for amenity in models.storage.all(Amenity).values():
                if amenity.id in self.amenity_ids:
                    amenity_list.append(amenity)
            return amenity_list

        @amenities.setter
        def amenities(self, obj):
            """Adds an amenity to the list"""
            if isinstance(obj, Amenity):
                self.amenity_ids.append(obj.id)


place_amenity = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)
