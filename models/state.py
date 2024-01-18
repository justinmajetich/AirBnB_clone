#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
# import models


class State(BaseModel, Base):
    """ State class """
    # name = ""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    # def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
    if models.storage_type == 'db':
        cities = relationship(
            'City',
            backref='state',
            cascade='all, delete-orphan'
        )
    elif models.storage_type == 'fs':
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances with
            state_id equals to the current State.id"""
            cities_list = []
            for city_id, city in models.storage.all('City').items():
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
