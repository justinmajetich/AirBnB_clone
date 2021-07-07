#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place, place_amenity


class Amenity(BaseModel, Base):
    """Amenity class"""
    __tablename__ = 'amenities'  # punto 10
    name = Column(String(128), nullable=False)  # punto 10
    place_amenities = relationship("Place", secondary=place_amenity)
