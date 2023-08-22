#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Columns, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel):
    """ State class for storing state information"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    if models.storage_type == 'db':
       cities = relationship("City", cascade="all, delete", back_populates="state")
    else:
       @property
        def cities(self):
            from models import storage
            from models.city import City
            all_cities = storage.all(City)
            return [city for city in all_cities.values() if city.state_id == self.id]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
