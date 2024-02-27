#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """attribute getter for FileStorage"""
            from models import storage
            from models.city import city
            city_list = []
            for city in storage.all(City).values():
                if city.state.id == self.id:
                    city_list.append(city)
            return city_list