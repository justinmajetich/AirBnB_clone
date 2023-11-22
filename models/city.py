#!/usr/bin/python3
""" City Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        __tablename__ = "cities"
        state_id = Column(String(60), nullable=False)
        name = Column(String(128), nullable=False)
else:
    class City(BaseModel):
        """The city class, contains state ID and name"""
        state_id = ""
        name = ""
