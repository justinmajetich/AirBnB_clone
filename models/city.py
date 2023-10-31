#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship
from os import getenv


HBNB_TYPE_STORAGE = getenv('HBNB_TYPE_STORAGE')


class City(BaseModel, Base):
    """The city class, contains state ID and name"""
    __tablename__ = 'cities'

    if HBNB_TYPE_STORAGE == "db":
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship(
            "Place",
            backref="cities", cascade="delete"
        )
    else:
        state_id = ""
        name = ""
