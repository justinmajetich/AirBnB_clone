#!/usr/bin/python3
""" Place Module for HBNB project """
import os
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.amenity import Amenity
from models import storage


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__="places"
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
    reviews = relationship("Review", backref='place', cascade="delete")
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False, back_populates="place_amenities")
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def amenities(self):
            """get all amenities"""

            amenities = list(storage.all(Amenity).values())
            return list(
                filter(lambda amenity: (amenity.place_id in self.amenity_ids),
                       amenities))  

        @amenities.setter
        def amenities(self, value=None):
            """add amenity id"""
            if type(value) == type(Amenity):
                self.amenity_ids.append(value.id)    
