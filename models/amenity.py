#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    """Amenity class representation"""
    __tablename__ = "amenities"
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        places = relationship(
            "Place",
            secondary=place_amenity,
            back_populates="amenities",
            viewonly=False
        )

    else:
        name = ""
