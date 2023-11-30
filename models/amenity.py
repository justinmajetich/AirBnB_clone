#!/usr/bin/python3
"""
    State Module for HBNB project
    *Update 1/12/2023: added code to use db storage and associated imports
        part of question 10
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'amenities'
        name = Column(String(128), nullable=False)
        place_amenities = relationship("Place", secondary="place_amenity",
                                       viewonly=False)
    else:
        name = ""
