#!/usr/bin/python3

""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv
from models.city import City

storageType = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if storageType == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """getter for cities"""
            from models import storage
            City = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    City.append(city)
            return City
