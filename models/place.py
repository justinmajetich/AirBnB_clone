#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Table
from sqlalchemy.orm import relationship
from os import getenv
import models


metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_Key=True,
                             nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_Key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """this is representation of place"""
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'),  nullable=False)
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

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        amenities = relationship("Amenity", secondary=place_amenity,
                                 viewonly=False,
                                 back_populates="place_amenities"))
    else:
        @property
        def reviews(self):
            """ Returns review objects
            """
            newlist = []
            for review in models.storage.all(Review):
                if review.place_id == self.id:
                    newlist.append(review)
            return newlist

        @property
        def amenities(self):
            """ Returns amenities objects
            """
            newlist = []
            for amenity in models.storage.all(Amenity):
                if amenity.id in amenity_ids:
                    newlist.append(amenity)
            return newlist

        @amenities.setter
        def amenities(self, obj):
            if type(obj) == Amenity:
                amenity_ids.append(obj.id)
