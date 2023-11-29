#!/usr/bin/python3
"""Module State hbnb"""
from sqlalchemy import Column, String,. Integer, Foreignkey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from models.city import City

class State(BaseModel, Base):
    """State Class"""
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")

    else:
        name = ' '
        @property
        def cities(self):
            city_list = []
            all_cities=models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
