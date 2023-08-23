#!/usr/bin/python3
"""Defines the State class."""

import models
from os import getenv
from models.base_model import Base, BaseModel
from models.city import City, Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """a state for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        __tablename__ (str): the MySQL table to store States.
        name (sqlalchemy String): name of the State.
        cities (sqlalchemy relationship): State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City",  backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list