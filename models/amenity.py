#!/usr/bin/python3
"""Defines the Amenity class."""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """
        this is the Amenity model

        Inherits:
            Basemodel
            Base
        Attributes:
        __tablename__: table name
        name: amenity name.
        place_amenities: Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)

