#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ The Amenity class, contains state ID and name """
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
