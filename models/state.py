#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship, backref
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        '''
        getter attribute cities that returns the list of City
        instances with state_id equals to the current State.id
        '''
        city_list = []
        all_cities = models.storage.all(City)
        for key in all_cities.keys():
            if all_cities[key].state_id == self.id:
                city_list.append(key)
        return city_list
