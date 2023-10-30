#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """State class repr states"""
    __tablename__ = 'states'

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                            cascade = "all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            from models import storage
            city_instances = storage.all(City)
            return [city for city in storage.values()
                    if city.state.id == self.id]
