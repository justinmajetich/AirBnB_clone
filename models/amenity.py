#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import column, String
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    """
    Class of Amenity
    """
    __tablename__ = "amenities"
    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        places_amenities = relationship("place",
                                        secondary='place_amenity')
        name = column(String(128), nullable=False)
    else:
        name=""
