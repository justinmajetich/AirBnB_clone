#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, text
from os import getenv


class State(BaseModel, Base):
    """ State class """

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column (String(128), nullable=False)
        cities = relationship('City', cascade='all, delete', backref='state')
    else:
        @property
        def cities(self):
            """getter attribute that returns the list of City instances"""
            from models import storage
            from models.city import City
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
