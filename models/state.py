#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', passive_deletes=True, backref='state')
    else:
        name = ""

    @property
    def cities(self):
        """
        Returns a list of City in the current State
        """
        city_list = []
        for city in models.storage.all('City').values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
