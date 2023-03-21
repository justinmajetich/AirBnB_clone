#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', back_populates="state")
    state = relationship('State', back_populates="City")

    name = ""

    if getenv("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            """Returning the cities in the current state"""
            from models import storage
            city_list = []
            for city in list(storage.all().values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
