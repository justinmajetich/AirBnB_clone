#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    Amenity inherits from BaseModel and Base 
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    places_amenities = relationship(
        "Place",
        secondary="place_amenity")
