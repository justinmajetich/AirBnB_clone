#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex



class State(BaseModel, Base):
    """
    State class
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(var[key])
        for elem in lista:
            if (elem.state_id == self.id):
                result.append(elem)
        return (result)

"""class State(BaseModel, Base):
    # State class
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if models.storage_type == 'db':
        cities = relationship(
            'City',
            backref='state',
            cascade='all, delete-orphan'
        )
    elif models.storage_type == 'fs':
        @property
        def cities(self):
            # Getter attribute that returns the list of City instances with
            # state_id equals to the current State.id
            cities_list = []
            for city_id, city in models.storage.all('City').items():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list"""
