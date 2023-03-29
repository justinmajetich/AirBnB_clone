#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class inherits from BaseModel and Base
    name (string): state name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    @property
    def cities(self):
        """Returns the list of City instances"""
        city_list = []
        cities = storage.all(City)
        for city in cities.values():
            if self.id == city.state_id:
                city_list.append(city)
        return city_list
