#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String

class City(BaseModel):
    """ The city class, contains state ID and name """
    __tablesname__ = 'cities'
    state_id = Column(String(60), nullable=False, primary_key=False)
    name = Column(String(128), nullable=False)
