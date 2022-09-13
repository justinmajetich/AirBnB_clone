#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import Base, BaseModel
from os import getenv
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from models.city import City


class State(BaseModel, Base):

    """Representation of state"""

    if models.storage == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship(
            "City", backref="state", cascade="all, delete, delete-orphan"
        )
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if models.storage != "db":

        @property
        def cities(self):
            """getter attribute cities that returns the list of City
            instances with state_id equals to the current State.id"""
            list_cities = []
            for key, value in models.storage.all(City).items():
                if value.state_id == self.id:
                    list_cities.append(value)
            return list_cities
