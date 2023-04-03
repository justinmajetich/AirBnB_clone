#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="states")
    else:
        name = ""

        @property
        def cities(self):
            """getter attribute cities that returns the list of
            City instances with
            state_id equals to the current State.id"""
            from models import storage
            from models.city import City
            city_list = []
            all_city = storage.all(City)
            for _, v in all_city.items():
                if self.id == v.state_id:
                    city_list.append(v)
            return city_list
