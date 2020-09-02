#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import os
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
        # cities is a list with relationship between city and state
        cities = relationship(
            "City", cascade="all, delete-orphan", backref="state")

        @property
        def cities(self):
            """Getter attribute"""
            return type(self).cities
    else:
        name = ''

        @property
        def cities(self):
            """Getter attribute"""
            cities = []

            for key, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    cities.append(city)

            return cities
