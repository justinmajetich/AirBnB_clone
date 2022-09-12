#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, Integer
from sqlalchemy.orm import relationship
from models import storage
import os
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column('name', String(128), nullable=False)
    cities = relationship('City', back_populates="state")

    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            return [city for city in storage.all(City).values()
                    if city.state_id == self.id]


City.state = relationship('State', back_populates="cities")
