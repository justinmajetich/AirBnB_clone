#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
from os import getenv
import models
import os


if os.getenv("HBNB_TYPE_STORAGE") == 'db':

    class State(BaseModel, Base):
        """ State class """

        __tablename__ = "states"
        name = Column(String(128), nullable=False)

        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")

else:

    class State(BaseModel):
        """ File storage State """
        name = ""

        @property
        def cities(self):
            """
            Returns list of City instances with state id
            """

            list_cities = []
            for key, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
