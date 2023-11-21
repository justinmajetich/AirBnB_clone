#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import shlex
from models import hbnb_type_storage


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade='all, delete, delete-orphan')

    @property
    def cities(self):
        var = models.storage.all()
        all_cities = []
        result = []
        for key in var:
            city = key.replace('.', ' ')
            city = shlex.split(city)
            if (city[0] == 'City'):
                all_cities.append(var[key])
        for elements in all_cities:
            if elements.state_id == self.id:
                result.append(elements)
        return result
