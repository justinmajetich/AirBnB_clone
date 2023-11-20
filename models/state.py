#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage_type
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if storage_type == 'db':
        cities = relationship('City', backref='state',
                              cascade='all, delete, delete-orphan')
    else:
        
        @property
        def cities(self):
            '''
            Returns the list of City instances with state_id
            equals the current State.id
            State.id is the FileStorage relationship between State and City
            '''
            from models import storage
            from models.city import City
            related_cities = []
            cities = storage.all(City)
            for city in cities.values():
                if city.state_id == self.id:
                    related_cities.append(city)
            return related_cities
