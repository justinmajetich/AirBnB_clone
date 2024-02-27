#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.base_model import BaseModel, Base

env = getenv('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    # Define the relationship with Place objects
    __tablename__ = 'cities'
    if env == 'db':
        places = relationship("Place", backref="cities", cascade="all, delete")
        state_id = Column(String(60), ForeignKey('states.id'))
        name = Column(String(128), nullable=False)
    else:
        name = ""
        state_id = ""
