#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage
import os

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    # For DBStorage
    if storage.storage_type == 'db':
        cities = relationship("City", backref="state", cascade="all, delete-orphan")

    # For FileStorage
    if storage.storage_type == 'file':
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances."""
            from models import storage
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
