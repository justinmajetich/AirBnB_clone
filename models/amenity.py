#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class with attributes"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    # Relationship with Place via place_amenity table
    places_amenities = relationship("Place", secondary='place_amenity',
                          back_populates="amenities")
