#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class Amenity(BaseModel):
    """Update Amenity"""
    __tablename__ = 'amenities'
    if (getenv('HBNB_TYPE_STORAGE') == 'db'):
        name = Column(String(128), nullable=False)
        place_amenity = relationship('Place', 'Amenity')
