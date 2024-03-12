#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
import models
import shlex


class State(BaseModel, Base):
    """ State class that contains name attribute
        Inherits from Basemodel and Base """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete-orphan",
                          backref="state")

    @property
    def cities(self):
        """add a public getter method cities to
        return the list of City"""
        val = models.storage.all()
        tmp = []
        final = []
        for key in val:
            cities = key.replace('.', ' ')
            cities = shlex.split(cities)
            if (cities[0] == 'City'):
                tmp.append(val[key])
        for elem in tmp:
            if (elem.state_id == self.id):
                final.append(elem)
        return (final)
