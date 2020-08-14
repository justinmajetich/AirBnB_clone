#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from models.engine.file_storage import FileStorage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete-orphan")

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        @property
        def cities(self):
            list_cities = []
            for c in FileStorage.all(City).values():
                if c.states_id == self.id:
                    list_cities.append(c)
            return list_cities
