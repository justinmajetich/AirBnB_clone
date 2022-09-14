#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
from models import storage


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """returns the list of City instances with state_id"""
            cities_list = []

            for k, city in storage.all(City).items():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list


