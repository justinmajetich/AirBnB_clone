#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import sys
from uuid import uuid4
import shlex
import models
from models.city import City
<<<<<<< HEAD
class State(BaseModel):
    """This is the class for State"""
    name = ""
    def __init__(self):
        super().__init__()
        self.id = str(uuid4())
=======
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel):
    """This is the class for State
    Attributes:
        name: input name"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

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
        return (result)
>>>>>>> 847b5534971cccde31dcb46c9e4c805f15d36be9
