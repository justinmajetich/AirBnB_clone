#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
import models.place


class Amenity(BaseModel, Base):
    """ Class for amenities"""
    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship(
        "Place",
        secondary='place_amenity',
        viewonly=False)
