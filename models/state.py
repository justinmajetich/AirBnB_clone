#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models
import shlex


class State(BaseModel, Base):
    """
    Represents a state for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    storage = getenv("HBNB_TYPE_STORAGE")

    if storage is None:
        storage = "fs"

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if storage == 'fs':
        @property
        def cities(self):
            """return the cities of the current state"""
            var = models.storage.all()
            lista = []
            result = []
            for key in var:
                city = key.replace('.', ' ')
                city = shlex.split(city)
                if (city[0] == 'City'):
                    lista.append(var[key])
            for elem in lista:
                if (elem.state_id == self.id):
                    result.append(elem)
            return (result)

    if storage == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
