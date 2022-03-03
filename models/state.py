#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
import os
from models import storage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City",
                              backref="state", cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            """getter that returns list of City instances with matching ids"""
            objects = storage.all(City)
            my_list = []
            for value in objects.values():
                if self.id == value.state_id:
                    my_list.append(value)
            return(my_list)
