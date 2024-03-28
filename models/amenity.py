#!/usr/bin/python3
""" This module defines the class Amenity """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Represents an amenity for a MySQL database.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    places_amenities = relationship("Place",
                                    secondary="place_amenity", viewonly=False)
