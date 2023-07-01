#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
import os
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import models


# HBNB_TYPE_STORAGE = os.getenv('HBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if models.HBNB_TYPE_STORAGE == 'db':
        cities = relationship("City", cascade="all, delete-orphan", backref="state")
    else:
        @property
        def cities(self):
            """city getter"""
            from models.city import City
            from models import storage

            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
