#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Add amenities"""

    __tablename__ = "amenities"
    if "db" == getenv("HBNB_TYPE_STORAGE"):
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
                            "Place",
                            secondary="place_amenity",
                            back_populates="amenities")

    else:
        name = ""
