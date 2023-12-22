#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade='all, delete-orphan',
                              backref='state')

    else:
        name = ""

        @property
        def cities(self):
            """returns City instances of the current State"""
            all_cities = models.storage.all('City').values()
            list_of_cities = []

            for city in all_cities:
                if city.state_id == self.id:
                    list_of_cities.append(city)
            return list_of_cities
