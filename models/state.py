#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',
                            cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        """Returns the list of City with state_id equals
        to the current State.id"""
        linked_cities = []
        cities = storage.all(City)
        for city in cities.values():
            if city.state_id == self.id:
                linked_cities.append(city)
        return linked_cities
