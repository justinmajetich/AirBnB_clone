#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import place_amenity
from sqlalchemy import Column, String, Table
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Stores Amenity information"""
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)

    place_amenities = relationship("Place", secondary="place_amenity",
                                   viewonly=False)
    # places = relationship(
    #     "Place", secondary=place_amenity,
    #     viewonly=False, back_populates="amenities"
    # )
