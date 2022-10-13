#!/usr/bin/python3
"""This is the state class"""
import os

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from base_model import BaseModel, Base




class State(BaseModel, Base):
    """This is the class for State
    Attributes:
    name: input name
    cities: relationship to cities table
    """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            'City', backref='state', cascade='all, delete-orphan'
        )
    else:
        @property
        def cities(self):
            """Get a list of cities associated with this state
            Return:
            return a list of all City instances with a state_id ma              
            """
            objects = models.storage.all(models.city.City)
            return [city for city in objects.values()
                    if city.state_id == self.id]
