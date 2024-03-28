#!/usr/bin/python3
"""Holds class Place"""

from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import Table
from sqlalchemy.sql.sqltypes import Float, Integer
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
import models
from os import getenv
from models.amenity import Amenity


# Association table for the Many-To-Many relationship between Place and Amenity
place_amenity = Table(
    'place_amenity', Base.metadata,
    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
)


class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []

    reviews = relationship(
        'Review', backref='place',
        cascade="all, delete, delete-orphan"
    )
    amenities = relationship(
        "Amenity", secondary=place_amenity, viewonly=False,
        backref="places"
    )

    @property
    def reviews(self):
        """Getter that returns the list of Review instances"""
        new = []
        for review in models.storage.all(Review).values():
            if review.place_id == self.id:
                new.append(review)
        return new

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def amenities(self):
            """FileStorage: Getter that returns the list of Amenity instances"""
            return [models.storage.all(Amenity)[id] for id in self.amenity_ids]

        @amenities.setter
        def amenities(self, obj):
            """FileStorage: Setter to add an Amenity.id to the amenity_ids list"""
            if type(obj) == Amenity:
                self.amenity_ids.append(obj.id)
