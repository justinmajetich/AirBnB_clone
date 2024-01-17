#!/usr/bin/python3
""" State class """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.city import City
import models
import shlex

class State(BaseModel, Base):
    """ State class
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
            cascade="all, delete, delete-delete")

    @property
    def cities(self):
        var = models.storage.all()
        lista = []
        result = []
        for key in var:
            city = key.replace('.', '')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lista.append(var[key])
        for element in lista:
            if (element.state_id == self.id):
                result.append(element)
        return (result)
