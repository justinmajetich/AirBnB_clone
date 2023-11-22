#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = "states"
        name = Column(String(128), nullable=False)

else:
    class State(BaseModel):
        """State class"""
        name = ""
