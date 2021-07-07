#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Float, Integer
from sqlalchemy.orm import relationship
from models.place import Place, place_amenity
import os


class Amenity(BaseModel, Base):
    """ Amenity class """
    if os.getenv('HBNB_ENV') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship('Place', secondary=place_amenity)
    else:
        name = ""
