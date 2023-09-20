#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column String Foreignkey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.__init__ import storage_type


class State(BaseModel, Base):
    """ 
    State class 
    """
    if storage_type == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationsip("City", backref="state")
    else:
        name = ""

    @property
    def cities(self):
        """ returns all
        the cities of the current state
        """
        my_cities = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                my_cities.append(city)
        return my_cities
