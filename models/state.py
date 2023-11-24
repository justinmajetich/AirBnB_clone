#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """ Getter for cities """
        from models import storage
        from models.city import City

        cities = storage.all(City)
        cities_list = []

        for city in cities.values():
            if city.state_id == self.id:
                cities_list.append(city)

        return cities_list
