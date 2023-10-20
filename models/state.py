#!/usr/bin/python3
"""Defines the State class."""
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """
        The state model
        Inherits:
            BaseModel
            Base
        Attributes:
            __tablename__: table name
            name: state name.
            cities:  State-City relationship.
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    citiess = relationship("City", backref="states", cascade="delete")

    database = getenv('HBNB_TYPE_STORAGE')
    if database != 'db':
        @property
        def cities(self):
            """get cities associated with state"""
            citys = []
            get_cities = models.storage.all(City).calues()
            for city in get_cities:
                if city.state_id == self.id:
                    citys.append(city)
            return citys
