#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        name = Column(String(60), nullable=False)
        cities = relationship('City', cascade='all, delete, delete-orphan', backref='state')
    else:
        name = ""

    """def __init__(self, *args, **kwargs):
        constructor for state class
        super().__init__(*args, **kwargs)"""

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """getter for list of city instances"""
            c_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    c_list.append(city)
            return c_list
