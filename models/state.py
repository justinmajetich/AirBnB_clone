#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            cities = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    cities.append(city)
            return  cities
