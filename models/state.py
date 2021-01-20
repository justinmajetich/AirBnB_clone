#!/usr/bin/python3
""" State class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, ForeignKey, Integer
from os import getenv
from models.city import City
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
    name: input name
    """
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        @property
        def cities(self):
            """Return list of city"""
            obj = models.storage.all(City)
            ls = []
            for city in obj.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
