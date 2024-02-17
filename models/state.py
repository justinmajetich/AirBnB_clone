#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',
                          cascade="all, delete-orphan")

    if models.env_stroage != 'db':
        @property
        def cities(self):
            """
            retrieve cities within a specific
            state
            """
            allcit = models.storage.all(City)
            return [city for city in allcit if city.state_id == self.id]
