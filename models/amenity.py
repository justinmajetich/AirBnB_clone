#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base



class Amenity(BaseModel, Base):
    """somthing"""
    from models.place import place_amenity
    __tablename__ = "Amenity"
    name = Column(String(128), nullable=False)
    place_amenity = relationship("Place", secondary=place_amenity, backref="amenities")