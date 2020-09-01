#!/usr/bin/python3
""" City Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from models.state import State
from sqlalchemy import Column, String, ForeignKey


if getenv("HBNB_TYPE_STORAGE") != "FileStorage":
    class City(BaseModel, Base):
        """ The city class, contains state ID and name """
        __tablename__ = 'cities'
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
else:
    class City(BaseModel):
        """ classes that inherit from BaseModel"""
        state_id = ""
        name = ""


