#!/usr/bin/python3
"""
    module containing Amenity class
"""
from models.base_model import BaseModel, Base
from models.city import City
from models.user import User
from models.place import place_amenity
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from os import environ

storage_engine = environ.get("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """
        Amenity class
    """

    if (storage_engine == "db"):
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place",
            secondary=place_amenity, back_populates="amenities")
    else:
        name = ""
