#!/usr/bin/python3
"""Here we have the state class"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
import models
from models.city import City
import shlex
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """This is the state class
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        test = models.storage.all()
        lis = []
        result = []
        for key in test:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lis.append(test[key])
        for i in lis:
            if (i.state_id == self.id):
                result.append(i)
        return (result)
