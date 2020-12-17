#!/usr/bin/python3
"""This is the place class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
import os
from sqlalchemy import Table
from models.review import Review
from sqlalchemy.orm import relationship
import models.amenity


class Place(BaseModel, Base):

    """ This is the class for Place and uses places table """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenity = Table('place_amenity', Base.metadata,
                              Column('place_id', String(60), ForeignKey(
                                 'places.id'), primary_key=True,
                                 nullable=False),
                              Column('amenity_id', String(60),
                                     ForeignKey('amenities.id'),
                                     primary_key=True,
                                     nullable=False))
        reviews = relationship(
            "Review", backref='place', cascade='all, delete-orphan')
        amenities = relationship(
            "Amenity", secondary=place_amenity, viewonly=False)
    else:
        @property
        def reviews(self):
            """ this is a getter that return rwlist """
            rwlist = []
            for rw in models.storage.all(Review):
                if rw.place_id == self.id:
                    rwlist.append(rw)
            return rwlist

        @property
        def amenities(self):
            """ this is a getter that return amtylist """
            amtylist = []
            for amy in models.storage.all(Amenity):
                if amy.id in amenity_ids:
                    amtylist.append(amy)
            return amtylist

        @amenities.setter
        def amenities(self, obj):
            if type(obj) == Amenity:
                amenity_ids.append(obj.id)
