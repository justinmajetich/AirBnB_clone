#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

from environ import get_env


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if get_env('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', back_populates='state', cascade='delete')
    
    if get_env('HBNB_TYPE_STORAGE') == 'file':
        @property
        def cities(self):
            '''returns a list of cities in ``self``'''
            from models import storage
            from city import City
            cities = storage.all(City)
            return [city for city in cities.values() if city.state_id == self.id]