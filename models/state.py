#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import models


class State(BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """gettet attribute for cities in FileStorage"""
            cities_list = []
            all_cities = models.storage.all(City)
            
            for city in all_cities.values():
                if city.state_if == self.id:
                    cities_list.appennd(city)
            return cities_list
