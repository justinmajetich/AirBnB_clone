#!/usr/bin/python3
"""This module defines a State class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import os

class State(BaseModel, Base):
    """This class defines a state"""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Get all City instances with state_id equals to current State.id"""
            all_cities = models.storage.all(City)
            state_cities = []
            for city in all_cities.values():
                if city.state_id == self.id:
                    state_cities.append(city)
            return state_cities
