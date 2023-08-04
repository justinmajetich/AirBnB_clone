#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Represents an Amenity for a MySQL.

    Inherits from SQLAlchemy Base and links to the MySQL table amenities.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store Amenities.
        name (sqlalchemy String): The amenity name.
        place_amenities (sqlalchemy relationship): Place-Amenity relationship.
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place",
                                   secondary="place_amenity",
                                   viewonly=False)
