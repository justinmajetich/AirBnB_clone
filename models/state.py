#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade='all, delete')


    if getenv("HBNB_TYPE_STORAGE") == 'fs':
        @property
        def cities(self):
            """Returning the cities in the current state"""
            from models import storage
            city_list = []
            for city in list(storage.all().values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
