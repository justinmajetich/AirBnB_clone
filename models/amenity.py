#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
import os
from sqlalchemy.orm import relationship


class Amenity(BaseModel):
    """represents the amenities in the place"""
    __tablename__ = 'amenities'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        place_amenities = relationship(
            "Place", backref="amenities", cascade="all, delete")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """intializes city"""
        super().__init__(*args, **kwargs)
