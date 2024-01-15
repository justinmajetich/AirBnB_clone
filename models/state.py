#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship("City", backref="state", cascade='all, delete')
    else:
        @property
        def cities(self):
            """getter for list of citis"""
            new_list = []
            all_cities = models.storage.all(City)
            for key in all_cities:
                if all_cities[key] == self.id:
                    new_list.append(all_cities[key])
            return new_list
