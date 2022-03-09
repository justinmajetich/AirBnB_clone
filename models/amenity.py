#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import Base, BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class Amenity(BaseModel, Base):
    """amenity class"""

    __tablename__ = "amenities"
    name = Column(String(128), nullable=False, unique=True)

    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        place_amenities = relationship("Place", secondary="place_amenity",
                                       viewonly=False,
                                       back_populates="amenities")
