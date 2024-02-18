#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        name = ''

    @property
    def cities(self):
        """getter funtion to get cities of certain state"""
        from models import storage
        city_dict = storage.all("City")
        state_cities = []
        for value in city_dict.values():
            if value.state_id == self.id:
                state_cities.append(value)
        return state_cities
