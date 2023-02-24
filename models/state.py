#!/usr/bin/python3
""" The state class"""
import os

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import city


class State(BaseModel, Base):
    """
    The class for State
    Attributes:
    name: input name
    """
   
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """ Returns the list of City instances with state_id
            equals to the current State.id. """
            all_cities = list(models.storage.all(City).values())
            return list(filter(lambda city: (city.id == self.id), all_cities))
