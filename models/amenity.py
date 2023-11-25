#!/usr/bin/python3
""" Amenity Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Defines an Amenity

    Attributes:
        __tablename__: represents the table name
        name: name of the Amenity instance
        place_amenities: many-to-many relationship between
                         places and amenities"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place",
                                   secondary="place_amenity",
                                   back_populates='amenities',
                                   viewonly=False)
