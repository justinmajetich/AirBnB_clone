#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    if getenv("HBNB_TYPE_STORAGE") == "file":
        @property
        def cities(self):
            """returns the list of City instances"""
            from models import storage
            return [city for city in storage.all("City").values() if city.state_id == self.id]
