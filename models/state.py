#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.city import City
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ Represents a state in MySQL DB

    Attributes:
        __tablename__ (str): name of the MySQL table to store states.
        name (string): name of the state.
        cities (string relationship): the state-city relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all city objects"""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
