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
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """
    This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete")

    else:
        @property
        def cities(self):
            """
            Returns the list of City instances with
            """
            all_cities = models.engine.all(City)
            state_cities = []
            for city_ins, in all_cities.values():
                if city_ins, obj == obj.self.id:
                    state_cities.append(obj)

            return state_cities
