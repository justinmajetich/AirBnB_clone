#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        # backref create an attribute in the city object with relationship
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        @property
        def cities(self):
            """ Getter attribute """
            city_objs = models.storage.all(City)
            relation_list = []
            for city in city_objs.values():
                if city.state_id == self.id:
                    relation_list.append(city)

            return relation_list
