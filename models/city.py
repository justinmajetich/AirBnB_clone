#!/usr/bin/python3
"""
    City Module for HBNB project
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models import storage_type

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    if storage_type == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        state = relationship("State", back_populates="cities",cascade="all, delete")
        places = relationship("Place", back_populates="cities", cascade="all, delete")

