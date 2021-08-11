#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """Getter cities"""
            cities = models.storage.all(City)
            list_cities = []
            for i in cities.values():
                if self.id == i.state_id:
                    list_cities.append(i)
            return list_cities
