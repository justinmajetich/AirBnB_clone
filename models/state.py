#!/usr/bin/python3
""" State Module for our hbnb project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel, Base):
    """ defines the class State """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')

    else:
        @property
        def cities(self):
            """ Returns the list of Cities"""
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]
