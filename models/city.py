#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


if getenv('HBNB_TYPE_STORAGE') == 'db':
    class City(BaseModel, Base):
        """The city class, contains state ID and name."""
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", backref="cities", cascade="all")

else:
    class City(BaseModel):
        """The city class, contains state ID and name."""
        state_id = ""
        name = ""
