#!/usr/bin/python3
""" State Module for HBNB project """

from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base


class Amenity(BaseModel, Base):
    """Amenities present in the airbnb"""

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place",
        secondary="place_amenity",
    )
