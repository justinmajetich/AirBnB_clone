#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade='all, delete, delete-orphan',
                              backref="state")
    else:
        @property
        def cities(self):
            from models import storage
            cities_list = []
            all_cities = storage.all("City")
            for city in all_cities.values():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
