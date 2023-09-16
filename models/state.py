#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    
    name = Column(String(128), nullable=False)
    cities = relationship(
            "City",
            backref="state",
            cascade="all, delete-orphan")
    
    @property
    def cities(self):
        """returns the list of City instances with state_id"""
        cities = models.storage.all(City)
        city_list = []
        for city in list(cities.values()):
            if city.state_id == self.id:
                    city_list.append(city)
        return city_list
