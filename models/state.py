#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ Creates the class: State

    Inherits from SQLAlchemy Base and links to states table

    Attributes:
        __tablename__ (str): The name of the table to use.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    __tablename__ = 'states'
    name = Column(String(128),
                  nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ Get a list of the related City objects."""
            c_list2 = []
            for city in list(models.storage.all('City').values()):
                if city.state_id == self.id:
                    c_list2.append(city)
            return c_list2
