#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128))
    cities = relationship("City",  backref="state")
    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
