#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel
from models.base_model import Base
from models.place import place_amenity

env = getenv('HBNB_TYPE_STORAGE')


class Amenity(BaseModel, Base):
    """Amenity model for HBNB"""

    __tablename__ = 'amenities'
    if env == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ""
