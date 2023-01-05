#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
# from models.state import State
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

# Inherits from both BaseModel and Base in that order


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'  # name of sql schema
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities",
                          cascade="all, delete, delete-orphan")
