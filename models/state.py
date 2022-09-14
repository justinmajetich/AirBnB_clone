#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        @property
        def cities(self):
            """ Returns the list of City instances with state_id equals
            to the current State.id """
            dict_city = models.storage.all(City)
            store = []
            for city in dict_city.values():
                if city.state_id == self.id:
                    store.append(city)
            return store
