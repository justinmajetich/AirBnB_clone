#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models import storage


class State(BaseModel, Base):
    """ State class

    Attributes:
        __tablename__: represents the table name, states
        name: name of the state
        cities: relationship to states"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """getter attributes cities return a list of
            cities within the current state"""
            city_list = []
            for city in list(storage.all(City).values()):
                if self.id == city.state_id:
                    city_list.append(city)
            return city_list
