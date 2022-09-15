#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from os import environ
from sqlalchemy.orm import relationship



class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'city'

    name = Column(String(128), nullable=False)
    state_id = Column((String(60), nullable=False, ForiegnKey('states.id'))
