#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import *
from sqlalchemy import Column, String, Integer, ForeignKey
from os import environ
from sqlalchemy.orm import relationship

storage = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if storage == 'db':
        name = Column(String(128), nullable=False)
    else:
        name = ''
