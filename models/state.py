#!/usr/bin/python3
""" State Module for HBNB project """

import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel):
    """ State class / table model """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            '''A getter method for cities from file storage'''
            cities = models.storage.all(City).values()
            cities_list = [city for city in cities if self.id == city.state_id]
            return cities_list
