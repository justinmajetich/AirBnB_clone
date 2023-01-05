#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import shlex


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """extractin and arranging the City contents"""
        var = models.storage.all()
        contents = []
        result = []
        for key in var:
            city = var.replace(',', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                contents.append(var[key])
        for elemnt in contents:
            if elemnt.state_id == self.id:
                result.append(elemnt)
        return result
