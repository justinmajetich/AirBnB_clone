#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(
        String(128),
        nullable=False
    )
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship(
            "City",
            backref="state", cascade="all,delete-orphan"
        )

    else:
        @property
        def cities(self):
            """returns list of City instances with state_id"""
            l_cities = []

            for city in models.storage.all(City).values():
                if self.id == city.state_id:
                    l_cities.append(city)

            return l_cities
