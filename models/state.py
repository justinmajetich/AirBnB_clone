#!/usr/bin/python3
"""Module State hbnb"""
from sqlalchemy import Column, String,. Integer, Foreignkey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models

class State(BaseModel, Base):
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if models.storage_type == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")
    elif models.storage_type == 'file':
        @property
        def cities(self):
            city_list = []
            for city in models.storage.all(City):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
