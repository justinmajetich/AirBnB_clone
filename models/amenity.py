#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, Float
from models.place import Place
from os import getenv


class Amenity(BaseModel, Base):
    """Amenities of the place"""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            'Place', secondary="place_amenity", back_populates="amenities")
    else:
        name = ""
