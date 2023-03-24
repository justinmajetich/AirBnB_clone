#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import shlex
import models
from models.city import City
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
from uuid import uuid4

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):

    """class for State
    Attributes
    """
    __tablename__ = "states"
    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")
    else:
        name =""
        state.id =""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)
        if not kwargs.get('id'):
            self.id = str(uuid4())

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