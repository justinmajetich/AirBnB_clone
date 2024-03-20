#!/usr/bin/python3
"""BACKUP VERSION"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
import models

class State(BaseModel, Base):
    """
    State class representing a geographical state.
    Attributes:
        name (str): The name of the state.
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        @property
        def cities(self):
            """
            Getter method for retrieving cities associated with the state.
            Returns:
                list: A list of City instances associated with the state.
            """
            st_cities = []
            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    st_cities.append(city)
            return st_cities