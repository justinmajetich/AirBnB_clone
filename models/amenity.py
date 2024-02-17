#!/usr/bin/python3

"""
Module for the Amenity class, representing an amenity in the application.
"""

from models import *
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Class representing an amenity in the application.
    Inherits from BaseModel and Base.
    """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """
        Initializes a new Amenity instance.
        Args:
            *args: Variable length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        super().__init__(*args, **kwargs)
