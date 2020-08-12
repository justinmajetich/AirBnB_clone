#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.place import Place
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """ Class Amenity """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship('Place', secondary='place_amenity')
