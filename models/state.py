#!/usr/bin/python3
"""This is the state class"""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        if models.storage.__class__.__name__ == 'DBStorage':
            return [
                    city for city in models.storage.all(City)
                    if city.state_id == self.id
            ]
        else:
            return [
                    city for city in models.storage.all(City)
                    if city.state_id == self.id
            ]
