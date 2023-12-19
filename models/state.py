#!/usr/bin/python3
"""
This modeule defines State class
"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """

    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'states'

        name = Column(String(128), nullable=False)
        cities = relationship(
            "City",
            cascade="all, delete-orphan",
            backref="state"
        )

    else:
        name = ""

    @property
    def cities(self):
        cities_list = []
        for city in models.storage.all(City).values():
            if city.state_id == self.id:
                cities_list.append(city)
        return cities_list
