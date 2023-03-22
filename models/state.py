#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
    if ('HBNB_TYPE_STORAGE' not in environ or
            environ["HBNB_TYPE_STORAGE"] != 'db'):
        @property
        def cities(self):
            """ Returns the list of City instances with state_id """
            from models.city import City
            from models import storage
            cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    cities.append(city)
            return cities
