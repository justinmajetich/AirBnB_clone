#!/usr/bin/python3
"""
This is the state class
"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, backref
import models
from os import getenv


class State(BaseModel, Base):
    """
    This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete")
    if getenv('HBNB_TYPE_STORAGE') == "db":


    # else:
        @property
        def cities(self):
            """
            Returns the list of City instances with
            state_id == current State.id
            """
            all_cities = models.storage.all(City)
            state_cities = []
            for city_ins in list(all_cities.values()):
                if self.id == city_ins.state_id:
                    state_cities.append(city_ins)

            return state_cities
