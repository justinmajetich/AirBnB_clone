#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(
        "City",
        backref="state",
        cascade="all, delete, delete-orphan"
    )

    @property
    def cities(self):
        """Getter method for cities property"""
        return [city for city in models.storage.all(City).values()
                if city.state_id == self.id]
