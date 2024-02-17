#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        @property
        def cities(self):
            """define City list instances"""
            city_list = []
            city_dic = models.storage.all(City)
            for city in city_dic.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return (city_list)
