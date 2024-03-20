#!/usr/bin/python3
"""Defines the State class"""

from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String

class State(BaseModel, Base):
    """Represents a state in the system"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade='all, delete, delete-orphan',
                          backref="state")

    @property
    def cities(self):
        """Returns the list of cities associated with this state"""
        return [city for city in self.cities]
