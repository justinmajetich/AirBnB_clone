#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os
from models.__init__ import storage
from models.city import City
class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    if  os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete-orphan")
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