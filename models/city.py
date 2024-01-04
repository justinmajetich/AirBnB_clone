#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from os import getenv
import models


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship(
            'Place',
            cascade="all, delete, delete-orphan",
            backref="cities")

    else:
        name = ""
        state_id = ""

    def __init__(self, *args, **kwargs):
        """initializes city"""
        super().__init__(*args, **kwargs)
