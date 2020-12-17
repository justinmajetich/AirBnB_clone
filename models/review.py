#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ State amenity"""
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)

    place_amenities = relationship("Place", secondary="place_amenity")
