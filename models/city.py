#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy import ForeignKey
from models import type_of_storage


class City(BaseModel, Base):
    """ The city class, contains state ID and name """

    __tablename__ = "cities"

    if type_of_storage == 'db':
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
    else:
        state_id = ''
        name = ''
