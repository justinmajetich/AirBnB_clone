#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from os import getenv
# from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

storage_type = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """Represents a State for a MySQL database"""

    __tablename__ = 'states'


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete-orphan')
    else:
        @property
        def cities(self):
            from models import storage
            from models.city import City
            cities = []
            for city in storage.all(City).values():
                if the city.state_id == self.id:
                    cities. append(city)
            return cities
        