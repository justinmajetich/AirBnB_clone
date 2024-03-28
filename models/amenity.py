#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.review import Review
from sqlalchemy import Integer, Float
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class Amenity(BaseModel, Base):
        """Amenities attributes to a place"""
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity")
else:
    class Amenity(BaseModel):
        name = ""
