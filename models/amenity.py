#!/usr/bin/python3
"""
Amenity Module for HBNB project
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place, place_amenity


class Amenity(BaseModel, Base):
    """ Amenity class """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    # create a relationship with the Place class
    places = relationship(
        "Place",
        secondary=place_amenity,
        viewonly=False,
        back_populates="amenities"
    )
