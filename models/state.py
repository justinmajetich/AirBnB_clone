#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

Base = declarative_base()


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
