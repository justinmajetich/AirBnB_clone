#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    name = Column(String(128), nullable=False)
    __tablename__ = 'states'
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete",
                backref="states")
    else:
        @property
        def cities(self):
            """returns City instances"""
            l_cities = models.storage.all("City").values()
            city_state = []
            for city in l_cities:
                if city.state_id == self.id:
                    city_state.append(city)
            return city_state
