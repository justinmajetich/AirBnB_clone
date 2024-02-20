#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity")

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship("Place", secondary="place_amenity")
    else:
        @property
        def place_amenities(self):
            """Getter attribute in case of file storage"""
            from models import storage
            from models.place import Place
            place_list = []
            for place in storage.all(Place).values():
                if place.amenity_id == self.id:
                    place_list.append(place)
            return place_list
        
