#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            "City",
            backref="state", cascade="all,delete-orphan"
        )

    else:
        @property
        def cities(self):
            """
            Returns the cities
            """
            cities_list = []

            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    cities_list.append(city)

            return cities_list
