#!/usr/bin/python3
"""Defines the State class."""
import models
from models import city
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from os import getenv
storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """Represent a state."""
    __tablename__ = 'states'

    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            from models import storage
            citylist = []
            citiesAll = storage.all(city)
            for cities in citiesAll.values():
                if cities.state_id == self.id:
                    citylist.append(cities)
            return citylist
