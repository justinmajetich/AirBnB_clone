#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from slqalchemy import Column, Integer, String, ForegnKey


class Amenity(BaseModel, Base):
    __tablename__ = 'amenities'
    name = Column(String(128), nullable=False)
    place_amenities = 

