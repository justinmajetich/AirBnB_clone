#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from os import getenv


class City(BaseModel, Base if (getenv("HBNB_TYPE_STORAGE")=="db") else object):
    """ The city class, contains state ID and name """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'cities'
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        places = relationship(
            "Place",
            cascade="all",
            backref=backref("cities", cascade="all"),
            passive_deletes=True
        )
    else:
        state_id = ""
        name = ""