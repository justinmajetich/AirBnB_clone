#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """State class repr states"""
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",cascade="all, delete-orphan")

    if getenv("HBNB_TYPE_STORAGE") == "db":
        @property
        def cities(self):
            list_cities = []
            from models import storage
            for object in models.storage.all(City).values():
                if object.state_id == self.id:
                    list_cities.append(object)
            return object
