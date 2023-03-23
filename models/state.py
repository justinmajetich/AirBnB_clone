#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', cascade="all, delete", backref="state")
    else:
        name = ""

    @property
    def cities(self):
        cities_list = []
        for city in models.storage.all(City).values():
            if self.id == city.state_id:
                cities_list.append(city)
        return cities_list
