#!/usr/bin/python3
"""State class for AirBnb v2 project"""
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class that creates states table"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, \
                              delete-orphan")

    else:
        @property
        def cities(self):
            """Cities getter"""
            citiesList = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    citiesList.append(city)
            return citiesList