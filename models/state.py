#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from models.city import City
import models
import os


class State(BaseModel, Base):

    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    # cities = relationship("City", cascade="delete")
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City', backref='state', cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            """Returns cities obj
            """
            newlist = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    newlist.append(city)
            return (newlist)
