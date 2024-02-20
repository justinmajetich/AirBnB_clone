#!/usr/bin/python3
""" State Module for HBNB project """

import os
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel

storage_type = os.getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """
    A class representing the Amenities

    Attributes:
      name (str)
    """
    __tablename__ = "amenities"

    name = ""

    if storage_type == "db":
        name = Column(String(128), nullable=False)
