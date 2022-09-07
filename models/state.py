#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime
from os import getenv
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='State', cascade='delete')
    else:

        @property
        def cities(self):
            """getter method"""
            city_list = []

            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
