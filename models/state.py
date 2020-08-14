#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if os.getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """Returns the list of City instances for current state"""
            from models import storage

            state_cities = []
            cities_all = models.storage.all(City)
            for city in cities_all.values():
                if city.state_id == self.id:
                    state_cities.append(city)
            return state_cities
