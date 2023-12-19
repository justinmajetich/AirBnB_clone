#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from os import getenv

strg = getenv("HBNB_TYPE_STORAGE")

class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'

    if strg == "db":
        state_id = Column(String(60), nullable=False, ForeignKey('states.id'))
        name = Column(String(128), nullable=False)
    else:
        name = ""
        state_id = ""
