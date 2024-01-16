#!/usr/bin/python3
"""
State module
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
from models import storage_type

class State(BaseModel):
    """
    State class that inherit from BaseModel
    """
    if storageType == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """ Getter method that gets a
            list of cities with the same stateid
            """
            allCities = storage.all(city)
            citiesList = [city for city in allCities.values()
                          if city.state_id == self.id]
            return citiesList
