#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from os import getenv 
from models import storage
from models.city import City

class State(BaseModel, Base):
    """ State class """
    
    
    if getenv("HBNB_TYPE_STORAGE") == "db":
    
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade='all, delete, delete-orphan',
                               backref="state")
    else:    
        name = ""
    if getenv("HBNB_TYPE_STORAGE") == "db":
        @property
        def cities(self):
            """getter attribute that returns the
              list of City instances with state_id equals to the current State.id"""
            
            cities_list = []
            all_cities = storage.all(City)
            for city in all_cities.values():
                if city.place_id == self.id:
                    cities_list.append(city)
            return cities_list