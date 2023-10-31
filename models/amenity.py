#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import place_amenity
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """ Repr of Amenity """
    __tablename__ = 'amenities'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)

    place_amenities = relationship(
        "Place", secondary="place_amenity", viewonly=False)
