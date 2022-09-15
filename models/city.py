#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship

storage = getenv('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'city'
    if storage == 'db':
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('state.id'), nullable=False)
    else:
        state_id = ''
        name = ''
