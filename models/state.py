#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    if models.storage_type == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""
        state_id = ""

        @property
        def cities(self):
            '''Retrieves all cities of the current state instance'''
            all_cities = models.storage.all('City').values()
            return [city for city in all_cities if city.state_id == self.id]
