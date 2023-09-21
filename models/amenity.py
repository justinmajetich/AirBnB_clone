#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import Base, BaseModel
from sqlalchemy import Column, String, Table, ForeignKey
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity Class"""

    __tablename__ = "amenities"
    if getenv("HBNB_TYPE_STORAGE"):

        name = Column(String(128), nullable=False)

    else:
        name = ""
