#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import column, String, Nullable
from sqlalchemy.orm import relationship
import models
class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = column(String(128), Nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    @property
    def cities(self):
        """ return list of the cities """
        cities= []
        for city in models.storage.all("cities").values():
            if city.state.id == self.id:
                cities.append(city)
        return cities

        
