#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """ Class attributes"""
    __tablename__ = "states"

    if environ['HBNB_TYPE_STORAGE'] == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """
            getter attribute cities that returns list of City instances
            with state_id equals to the current State.id -> it will be
            the FileStorage relationship between State and City
            """
            from models import storage
            from models.city import City
            """returns list of City objs in __objects"""
            cities_dict = storage.all(City)
            cities_list = []

            """copy values from dict to list"""
            for city in cities_dict.values():
                if city.state_id == self.id:
                    cities_list.append(city)

            return cities_list
