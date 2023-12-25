#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """
    Amenity inherits from BaseModel and Base (respect the order)
    class attribute __tablename__ represents the table name, amenities
    class attribute name represents
    a column containing a string (128 characters) can’t be null
    class attribute place_amenities must represent a relationship
    Many-To-Many between the class Place and Amenity."""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
