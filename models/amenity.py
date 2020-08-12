#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import place_amenity
import os


class Amenity(BaseModel, Base):
    """Object representation of table amenities
    """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place",
            secondary=place_amenity
        )
    else:
        name = ""
