#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage as s

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if s.__class__.__name__ == 'DBStorage':
        cities = relationship("City", back_populates='state', cascade='delete, delete-orphan')

    elif s.__class__.__name__ == 'FileStorage':
        @property
        def cities(self):
            """Getter attribute that returns the list of City instances"""
            from models import storage
            from models.city import City
            city_inst = storage.all(City)
            return [city for city in city_inst.values() if city.state_id == self.id]