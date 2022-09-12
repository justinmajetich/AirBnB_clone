#!/usr/bin/python3
""" State Module for HBNB project """
import models

from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlachemy import Column, String, Foreignkey
from sqlachemy import.orm import relationship



class Amenity(BaseModel, Base):
    """Implements the Amenity model"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "amenities"
        name = Column(String(128), nullable=False)
    # place_amenities = relationship("Place", secondary=place_amenity)

    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initialize amenities"""
        super().__init__(*args, **kwargs)
