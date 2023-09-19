#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City


env_strg = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    if env_strg == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        name = ''

        @property
        def cities(self):
            from models import storage
            cityStrg = storage.all(City)
            cityList = []
            for city in cityStrg:
                if self.id == city.state_id:
                    cityList.append(city)
            return cityList
