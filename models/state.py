#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:

        @property
        def cities(self):
            """Getter attribute cities that returns the list of City instances"""
            city_list = []
            for city in models.storage.all(City).values():
                if (self.id == city.state_id):
                    city_list.append(city)
            return city_list
