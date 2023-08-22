#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
import shlex


class State(BaseModel, Base):
    """State class inherits from BaseModel, Base
    Attributes:
        name: string(128)
        cities: relationship with City class
    """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        var = models.storage.all()
        lis = []
        res = []
        for k in var:
            city = k.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                lis.append(var[k])
        for city in lis:
            if (city.state_id == self.id):
                res.append(city)
        return (res)
