#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    if (getenv("HBNB_TYPE_STORAGE") == "db"):
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        @property
        def cities(self):
            """returns the list of city instance with sate_id
            equals the current state.id
            fileStorage relationship between state and city
            """
            from models import storage
            related_cities = []

            cities = storage.all(City)
            for key, value in cities.items():
                if value.state_id == self.id:
                    related_cities.append(value)
            return related_cities
