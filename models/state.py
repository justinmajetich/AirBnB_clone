#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
import models
from models.city import City
import shlex
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Session
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name"""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    state_id = Column(String(128), nullable=False)

    @property
    def cities(self):
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(var[key])
        for elem in lista:
            if (elem.state_id == self.id):
                result.append(elem)
        return result
