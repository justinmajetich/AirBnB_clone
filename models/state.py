#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage_type


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ''

    @property
    def cities(self):
        """Returns the list of City instances with state_id equals
           to the current State.id => It will be the FileStorage
           relationship between State and City
        """
        from models import storage
        filtered_cities = []
        cities = storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                filtered_cities.append(city)
        return filtered_cities  # returns cities with same state id
