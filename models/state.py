#!/usr/bin/python3
""" State Module for HBNB project """
import models
from os import getenv
import sqlalchemy
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="states", cascade="all, delete")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ Getter attribute cities that returns the list of City instances
            with state_id equals to the current State.id """
            city_instances = models.storage.all("City").values()
            city_list = list()
            for city in city_instances:
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
