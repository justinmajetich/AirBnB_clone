#!/usr/bin/python3
"""Amenity class"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """amenity class"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenity = relationship(
        'Place', secondary=place_amenity)
