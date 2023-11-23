#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from models import storage_type


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    if storage_type == 'db':
        state_id = Column(String(128), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        name = ''
        state_id = ''
