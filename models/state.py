#!/usr/bin/python3
'''
    Implementation of the State class
'''
from os import getenv
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models


class State(BaseModel, Base):
    '''
        Implementation for the State.
        Create relationship between class State (parent) to City (child)
    '''
    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            '''
                Return list of city instances if City.state_id==current
                State.id
                FileStorage relationship between State and City
            '''
            list_cities = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities
