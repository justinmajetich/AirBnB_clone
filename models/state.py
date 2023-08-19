#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if environ.get('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='states', cascade='all, delete')
    else:
        @property
        def cities(self):
            from models import storage
            cities = []
            for city in storage.all(City):
                city_obj = storage.all()[city]
                if city_obj.__dict__['state_id'] == self.id:
                    cities.append(city_obj)
            return cities
