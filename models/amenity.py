#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Relationship
import models
from sqlalchemy import (
    Column,
    String,
)


class Amenity(BaseModel, Base):
    """ Amenity class to store amenity information """
    if models.storage_type == "db":
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
        place_amenities = Relationship(
            "Place", secondary="place_amenity", backref="amenity"
        )
    else:
        name = ""
