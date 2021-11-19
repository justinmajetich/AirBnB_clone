#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from os import getenv
from sqlalchemy.orm import relationship
from models.city import City
from models import storage

class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv(HBNB_TYPE_STORAGE) == "db":
        cities = relationship('City', cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            """getter for cities list when using filestorage"""
            return [city for city in storage.all("City").values()
                    if city.state_id == self.id]
