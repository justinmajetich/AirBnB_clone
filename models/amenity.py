#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """Amenity model for HBNB"""

    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
            "Place",
            secondary="place_amenity",
            backref="amenities"
        )
