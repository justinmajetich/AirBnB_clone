#!/usr/bin/python3
"""This script defines the Amenity class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Represents an amenity in a MySQL database.

    Inherits from SQLAlchemy Base and is linked to the MySQL table 'amenities'.

    Attributes:
        __tablename__ (str): The name of the MySQL table for storing amenities.
        name (sqlalchemy String): The name of the amenity.
        place_amenities (sqlalchemy relationship): The Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)

