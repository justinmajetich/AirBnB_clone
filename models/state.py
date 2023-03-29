#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import relationship
from os import getenv

storage = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """State class"""
    if storage == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="delete")

    else:
        name = ""

        @property
        def cities(self):
            """Getter method"""
            city_list = []
            for city in models.storage.all("City").values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
