#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
from models.city import City
import models

class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        """returns the list of City instances with state_id"""
        all_cities = storage.all(City)
        cities = []
        for key, value in all_cities.items():
            if value.state_id == self.id:
                cities.append(value)
        return cities
