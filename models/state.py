#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.engine.file_storage import FileStorage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    def cities(self):
        """Returns the list of City instances for current state"""
        state_cities = []
        cities_all = Filestorage.all(City)
        for city in cities_all.values():
            if city.state_id == self.id:
                state_cities.append(city)
        return state_cities
