#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class Amenity(BaseModel, Base):
    """Amenity class representing an amenity provided by a place."""
    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)

    place_amenities = relationship("Place", secondary="place_amenity")
