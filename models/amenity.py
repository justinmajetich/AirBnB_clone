#!/usr/bin/python3
"""
0x00. AirBnB clone - The console
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
import os

STORAGE = os.getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """Permit to add the amenities for places"""
    __tablename__ = "amenities"
    if STORAGE == "db":
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            'Place', secondary=Place.place_amenity,
            viewonly=False)
    else:
        name = ""

