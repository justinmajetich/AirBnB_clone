#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os

STORAGE = os.getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    if STORAGE == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """Returns the cities"""
            from models import storage

            city_list = []
            for key, value in storage.all(City).items():
                if self.id == value.state_id:
                    city_list.append(value)
            return city_list
