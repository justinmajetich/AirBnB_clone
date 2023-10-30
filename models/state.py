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
            citys = storage.all(City)
            for k, v in citys.items():
                if v.state_id == self.id:
                    city_list.append(v)
            return city_list
