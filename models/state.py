#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete, delete-orphan")
    else:
        @property
        def cities(self):
            """returns the list of City instances with state_id equals
            to the current State.id"""
            obj = models.storage.all(City)
            ls = []
            for city in obj.values():
                if city.state_id == self.id:
                    ls.append(city)
            return ls
