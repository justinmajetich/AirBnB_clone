#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        __tablename__: name of MySQL table
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """Getter method for cities
            Return: list of cities with state_id equal to self.id
            """
            from models import storage
            from models.city import City
            # return list of City objs in __objects
            cities_dict = storage.all(City)
            cities_list = []

            # copy values from dict to list
            for city in cities_dict.values():
                if city.state_id == self.id:
                    cities_list.append(city)

            return cities_list
