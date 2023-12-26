#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
import sqlalchemy
from sqlalchemy import Column, String
from alchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    def init(self, *args, **kwargs):
        """initialize state"""
        super().__init__(*args, **kwargs)


    if getenv('HBNB_TYPE_STORAGE') != 'db':
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
