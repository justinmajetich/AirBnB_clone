#!/usr/bin/python3
"""Defines the State class."""
import models
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from models.city import City
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Represents a State"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related Cities."""
            city_l = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_l.append(city)
            return city_l
