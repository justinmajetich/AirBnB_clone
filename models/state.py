#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import create_engine, Column, String
from sqlalchemy.orm import relationship
from os import getenv

storage_type = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """Name of table in database to link to"""
    __tablename__ = "states"

    """This class defines a user by name & state_id attributes"""
    name = Column(String(128), nullable=False)

    if storage_type != "db":
        @property
        def cities(self):
            """
            Getter, returns list of City objects from storage linked
            to current State
            """
            city_objs = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_objs.append(city)
            return city_objs
    else:
        cities = relationship("City", backref="state", cascade="delete")
