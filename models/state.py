#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from models.city import City
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')

    if getenv('HBNB_TYPE_STORAGE') == 'fs':
        @property
        def cities(self):
            city_list = []
            for ob_id, city in models.storage.all(City).items():
                if self.id == city.state_id:
                    city_list.append(city)
            return city_list
