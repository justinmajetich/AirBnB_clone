#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':

        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all, delete", backref="state")
    else:
        name = ""

    @property
    def cities(self):
        """
            Returns the list of City instances with state_id equals
            to the current State.id
        """
        list_cities = []
        for city in models.storage.all(City).values():
            if self.id == city.state_id:
                list_cities.append(city)
        return list_cities
