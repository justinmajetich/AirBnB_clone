#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    # cities is a list with relationship between city and state
    cities = relationship(
        "City", cascade="all, delete-orphan", backref="state")

    @property
    def cities(self):
        """Getter attribute"""
        return type(self).cities
