#!/usr/bin/python3
"""State module for HBNB project"""

import models
import os
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """State class for HBNB project"""

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
            cities_in_state = []
            for value in models.storage.all(City).values():
                if value.state_id == self.id:
                    cities_in_state.append(value)
            return cities_in_state
