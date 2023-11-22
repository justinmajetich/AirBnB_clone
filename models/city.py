#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey

class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(128), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    base_id = Column(String, ForeignKey('base.id'), nullable=False)
