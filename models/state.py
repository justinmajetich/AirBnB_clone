#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
    @property
    def cities(self):
        """
            Returns the list of City instances with state_id equals
            to the current State.id
        """
        list_cities = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                list_cities.append(city)
        return list_cities
