#!/usr/bin/python3
"""This is the amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
import os


class Amenity(BaseModel, Base):

    """ This is Amenity class"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship("Place", secondary=Place.place_amenity,
                                       back_populates="amenities")
