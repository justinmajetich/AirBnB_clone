#!/usr/bin/python3
""" State Module for HBNB project """
import os

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

import models
from models.base_model import Base, BaseModel
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            "City",
            back_populates="state",
            cascade="all, delete, delete-orphan"
        )
    else:
        @property
        def cities(self):
            """Getter for cities."""
            cities_list = []
            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    cities_list.append(city)
            return cities_list
