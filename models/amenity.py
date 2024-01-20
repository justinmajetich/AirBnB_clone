#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """
    class amenity
    """
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    places = relationship('Place', secondary=place_amenity, back_populates='amenities', viewonly=False)
