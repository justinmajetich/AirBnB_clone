#!/usr/bin/python3
"""
Module for the new Amenity class
"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship


place_amenity = Table('place_amenity', Base.metadata,
                      Column('place_id', String(60),
                             ForeignKey('places.id'),
                             primary_key=True, nullable=False),
                      Column('amenity_id', String(60),
                             ForeignKey('amenities.id'),
                             primary_key=True, nullable=False)
                      )


class Amenity(BaseModel, Base):
    """
    Class that define Amenity based on BaseModel
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    """ Class attribute place_amenities must represent a relationship
    Many-To-Many between the class Place and Amenity"""
    place_amenities = relationship("Place", secondary='place_amenity',
                                   back_populates="_amenities")
