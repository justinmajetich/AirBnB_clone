#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel
from os import getenv
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """ State class for State """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')

else:
    class State(BaseModel):
        """ State class for State """
        name = ''

    @property
    def cities(self):
        """ Returns the list of `City` instances
        with `state_id` equals to the current
        """
        cities = []
        for key, value in models.storage.all(City).items():
            if value.state_id == self.id:
                cities.append(value)
        return cities
