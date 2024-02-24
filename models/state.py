#!/usr/bin/python3
""" State Module for the HBNB project."""
from models import storage_type
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """A class that defines a state rep"""
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128),
                      nullable=False)
        cities = relationship("City", cascade="all, delete, delete-orphan",
                              backref="state")
    else:
        name = ""

        @property
        def cities(self):
            """ Returns the no of cities where given
            state_id == to the current state_id."""
            from models import storage
            cities_related = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    cities_related.append(city)
            return cities_related
