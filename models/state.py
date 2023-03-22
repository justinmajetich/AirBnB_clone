#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class which contains __tablename__, name"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', base_populates='State',
                          cascade='all, delete')

    @property
    def cities(self):
        """getter attribute that returns the list of City instances
        with state_id equals to the current State.id"""
        cities_list = []
        for city in cities_list:
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
