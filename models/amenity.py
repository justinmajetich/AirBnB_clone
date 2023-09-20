#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import String, Column
from os import getenv

class Amenity(BaseModel):
    """
    Defines the Amenity model class for a given database
    """
    __tablename__ = "amenities"

    name = Column(String(255), nullable=False)
    place_amenities = relationship("place", secondary="place_amenity",
                                   viewonly=False)
