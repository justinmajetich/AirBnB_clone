#!/usr/bin/python3
"""
Define the ``Amenity`` class that inherits from the class ``BaseModel``
"""
from models.base_model import BaseModel
from models.base_model import Base
from models.base_model import (
        Column,
        String,
        relationship,
        Table)
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """
    Define the class Amenity

    * __tablename__: represents the table name, 'amenities'
    * name (String): represents a column containing a string (128 characters)
        * can’t be null

    # Relationship
    * place_amenities: represents a relationship 'Many-To-Many' between
        the class 'Place' and 'Amenity'.
    """
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)

    # Relationship:
    place_amenities = relationship("Place", secondary=place_amenity)
