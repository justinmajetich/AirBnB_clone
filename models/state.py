#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship('City', cascade="all, delete", backref='state')
    else:
        @property
        def cities(self):
            ''' getter for FileStorage cities-state '''
            from models import storage
            load = []
            all_cities = storage.all(City)
            for id_city, obj in all_cities.items():
                if self.id == obj.state_id:
                    load.append(obj)
            return load
