#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
import models
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
from os import getenv

storage = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if storage == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='states')
    else:
        name = ""
    if storage != 'db':
        @property
        def cities(self):
            """
            return list of cities
            """
            list_cities = []
            cities = models.storage.all(City)
            for key, city_obj in cities.items():
                if city_obj.state_id == self.id:
                    list_cities.append(city_obj)
            return list_cities
