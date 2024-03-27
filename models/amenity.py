#!/usr/bin/python3
""" This module defines the class Amenity """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Represents an amenity for a MySQL database.

    Public class atributes:
        __tablename__ (str): Name of MySQL table to store amnities.

        name (Columns: Str): Name of the city.
        state_id (Columns: Str): Foreign key to 'states.id'.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
