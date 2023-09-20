#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.place import Place


class Amenity(BaseModel):
    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)

    place_amenities = relationship(
        'Place',
        secondary=Place.place_amenity,
        back_populates='amenities'
    )
