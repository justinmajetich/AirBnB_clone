#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan',
                          passive_deletes=True)


if getenv('HBNB_TYPE_STORAGE') != 'db':
    @property
    def cities(self):
        """getter for cities"""
        from models import storage
        cities_list = []
        cities_dict = storage.all(City)
        for city in cities_dict.values():
            if self.id == city.state_id:
                cities_list.append(city)
        return cities_list
