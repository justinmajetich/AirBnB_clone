#!/usr/bin/python3
"""This is the state class"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_MYSQL_DB") == 'db':
        cities = relationship("City", cascade='all, delete', backref="state")
    else:
        @property
        def cities(self):
            my_list = []
            for data in models.storage.all(City).values():
                if data.state_id == self.id:
                    my_list.append(data)
            return(my_list)
