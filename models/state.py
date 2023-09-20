#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City",
                          backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """Getter method for cities."""
        city_objs = models.storage.all("City")
        return [city for city in city_objs.values(
            ) if city.state_id == self.id]
