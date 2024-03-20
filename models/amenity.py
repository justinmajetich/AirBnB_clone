#!/usr/bin/python3
"""
This module contains the Amenity class, which inherits
from the BaseModel class 
"""

from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """
    This class describes the Amenity model, a child of BaseClass on
    which amenity objects are based
    """

    __tablename__ = 'amenities'

    name = Column(String(128), nullable=False)
    place_amenities = relationship("Place", secondary="place_amenity")
