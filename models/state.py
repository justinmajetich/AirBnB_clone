#!/usr/bin/python3
"""Defines the State class."""
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String
import models


class State(BaseModel, Base):
    """Represents a state."""

    __tablename__ = "states"

    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Getter attribute that returns the list of City instances with
        the corresponding state_id."""
        all_cities = models.storage.all(City)
        state_cities = []
        for city in all_cities.values():
            if city.state_id == self.id:
                state_cities.append(city)
        return state_cities
