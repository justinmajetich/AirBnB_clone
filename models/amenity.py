#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Creates the class: Amenity:

    Inherits from SQLAlchemy Base and links to amenities table.

    Attributes:
        __tablename__ (str): The name of the table to use.
        name (sqlalchemy String): The name of the amenity.
        place_amenities (sqlalchemy): Place-Amenity relation.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
