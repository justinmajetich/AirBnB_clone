#!/usr/bin/python3
"""This is the amenity class"""
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from models.place import place_amenity


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary=place_amenity)
