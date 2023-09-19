#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="State")

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            import models
            cities_list = []
            all_cities_list = models.storage.all(City)
            for a_city in all_cities_list.values():
                if a_city.state_id == self.id:
                    cities_list.append(a_city)
            return cities_list