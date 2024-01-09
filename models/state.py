#!/usr/bin/python3
""" State Module for BnB v2 project """
import os
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(
        String(128), nullable=False
    ) if os.getenv('HBNB_TYPE_STORAGE') == 'db' else ''
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City',
            cascade='all, delete, delete-orphan',
            backref='state'
        )
    else:
        @property
        def cities(self):
            """Returns the cities in this State"""
            from models import storage
            cities_of_state = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    cities_of_state.append(value)
            return cities_of_state
