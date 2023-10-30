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
    if models.storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """Init city"""
        super().__init__(*args, **kwargs)

    if models.storage_t == "db":
        @property
        def cities(self):
            from models import storage
            city_instances = storage.all(City)
            return [city for city in storage.values()
                    if city.state.id == self.id]
