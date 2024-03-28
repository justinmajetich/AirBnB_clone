#!/usr/bin/python3
"""City Module for HBNB project"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class City(BaseModel, Base):
    """The city class, contains state ID and name"""
    __tablename__ = "cities"
    
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    
    # Only define the relationship if using db storage
    if getenv("HBNB_TYPE_STORAGE") == "db":
        places = relationship("Place", backref="cities", cascade="all, delete", passive_deletes=True)
