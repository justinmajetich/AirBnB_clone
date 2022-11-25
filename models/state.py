#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """getter attribute cities that returns the list of City"""
        from models import storage
        my_list = []
        extracted_cities = storage.all(City).values()
        for city in extracted_cities:
            if self.id == city.state_id:
                my_list.append(city)
        return my_list
