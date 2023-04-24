#!/usr/bin/python3
"""This is the state class"""
import os
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade='all, delete, '
                                              'delete-orphan', backref="state")

    else:
        @property
        def cities(self):
            """public getter method cities to return the list of City"""
            city_objs = models.storage.all(City).values()
            return [city for city in city_objs if city.state_id == self.id]
