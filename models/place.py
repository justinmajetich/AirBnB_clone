#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy import Table
from sqlalchemy.orm import relationship
import os


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    place_amenity = Table(
        "place_amenity", metadata,
        Column("place_id", String(60), ForeignKey('place.id'),
                primary_key=True, nullable=False),
        Column("amenity_id", String(60), ForeignKey('amenity.id'),
                primary_key=True, nullable=False))
    reviews = relationship(
        "Review",
        backref="place",
        cascade="all, delete-orphan")
    amenities = relationship(
        "Amenity",
        secondary=place_amenity,
        viewonly=False)

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            from models.review import Review

            list_reviews = []
            for c in FileStorage.all(Review).values():
                if c.place_id == self.id:
                    list_reviews.append(c)
            return list_reviews

        @property
        def amenities(self):
            from models.amenity import Amenity

            list_amenities = []
            for c in FileStorage.all(Amenity).values():
                if c.amenity_ids == Amenity.id:
                    list_amenities.append(c)
            return list_amenities

        @property.setter
        def amenities(self, value):
            from models.amenity import Amenity

            if type(value) is type(Amenity):
                self.amenity_ids.append(value.id)
