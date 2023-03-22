#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


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

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')


    if storage == 'fs':
        @property
        def cities(self):
            """Returning the cities in the current state"""
            from models import storage
            city_list = []
            for city in list(storage.all().values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
    if storage == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
