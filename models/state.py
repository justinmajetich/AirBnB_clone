#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    # check if the origin of the data is from db
    origin_data = os.getenv("HBNB_TYPE_STORAGE")
    # if come from db_storage
    if (origin_data == "db"):
        cities = relationship("City", backref="state", cascade="all, delete")
    # if come from file_storage
    else:
        @property
        def cities(self):
            """Getter attribute cities"""
            cities = models.storage.all(City)
            list_cities = []
            for idx_cities in cities.values():
                if self.id == idx_cities.state_id:
                    list_cities.append(idx_cities)
            return list_cities
