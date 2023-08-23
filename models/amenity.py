#!/usr/bin/python3
"""This is the Amenity class."""
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """shows an Amenity for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table amenities.

    Attributes:
        __tablename__ (str): the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)