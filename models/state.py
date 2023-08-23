#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models import storage_type
from uuid import uuid4


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
       if storage_type == 'db':
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        name = ''

        @property
        def cities(self):
            all_cities = models.storage.all(City)
            return [city for city in all_cities.values()
                    if city.state_id == self.id]
