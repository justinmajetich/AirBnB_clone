#!/usr/bin/python
""" holds class Place"""
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql.schema import Table
from sqlalchemy.sql.sqltypes import Float, Integer
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models.review import Review
import models
from os import getenv
from models.amenity import Amenity

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
        'Review',
        backref='state',
        cascade="all, delete, delete-orphan"
    )
    amenities = relationship("Amenity",
                             secondary='place_amenity', viewonly=False,
                             backref="place_amenities")

    @property
    def reviews(self):
        """ Getter that that returns the list of Reviews instances """
        instances = models.storage.all(Review)
        new = []
        for review in instances.values():
            if review.place_id == (self.id):
                new.append(review)
        return new

    @reviews.setter
    def amenities(self, obj):
        """
        Setter attribute amenities that handles append method
        for adding an Amenity.id to the attribute amenity_ids.
        """
        if isinstance(obj, Amenity):
            self.amenities.append(obj)
