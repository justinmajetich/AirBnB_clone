#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
import os



class Amenity(BaseModel, Base):
    """ Class Amenity """
    __tablename__ = amenities

    name = Column(String(128), nullable=False)
    place_amenities = ("Place", secondary=place_amenity) 

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship("Place", secondary=Place.place_amenity,
                                       back_populates="amenities")
