#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.sql.schema import ForeignKey
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        @property
        def cities(self):
            """"""""
            list_c = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    list_c.append(city)
            return list_c
