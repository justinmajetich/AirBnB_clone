#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from os import environ
from sqlalchemy.orm import relationship

class State(BaseModel,):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
