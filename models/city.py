#!/usr/bin/python3
"""This is HBNB the city class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from models.place import Place
from os import getenv


class City(BaseModel, Base):
    """This is the class for City
    """
    __tablename__ = "cities"

    if getenv('HBNB_TYPE_STORAGE') is not None:
        name = Column(String(128), nullable=False)
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        places = relationship("Place", cascade='all, delete',
                              backref="cities", passive_deletes=True)
    else:
        name = ""
        state_id = ""
