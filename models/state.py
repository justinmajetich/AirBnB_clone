#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state")

    if models.storage_t != "db":
        @property
        def cities(self):
            """ Getter for list of city instances related to the state """
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values(): 
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
