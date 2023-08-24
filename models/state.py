#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', back_populates='state',
            cascade='all, delete-orphan')
    name = ''

    @property
    def cities(self):
        """getter attribute cities that returns the list of
        City instances with state_id that equal to the current
        State.id"""
        from models import storage
        all_cities = storage.all('City').values()
        cities = []
        for city in all_cities:
            if city.state_id == self.id:
                cities.append(city)
        return cities
