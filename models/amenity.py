#!/usr/bin/python3
""" Amenity Class for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """`Amenity` represents details of an amenity in a place"""

    __tablename__ = "amenities"

    if storage_type == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""
