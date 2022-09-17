#!/usr/bin/python3
"""Define a class State that inherits from BaseModel."""
import models
from os import getenv
from models.city import City
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """Represents a state.
    Attributes:
        name (str): The name of the state.
    """

    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """Returns a list of all related City objects."""
            cities_list = []
            for k, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
            