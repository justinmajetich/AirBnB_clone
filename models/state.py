#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base

if getenv('HBNB_TYPE_STORAGE') == 'db':
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all")

else:
    class State(BaseModel):
        """ State class """
        name = ""

        @property
        def get_cities(self):
            from models import storage
            """Return the list of City instances"""
            cities_list = [items for items in
                           storage.all(City) if City.state_id == self.id]
            return cities_list
