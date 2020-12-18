#!/usr/bin/python3
"""
This is the state class without marge
"""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey, MetaData
from sqlalchemy.orm import relationship, backref
import models
from os import getenv
from sqlalchemy.ext.declarative import declarative_base


class State(BaseModel, Base):
    """
    This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == "db":
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete")

    else:
        @property
        def cities(self):
            """
            Returns the list of City instances with
            state_id == current State.id
            """
            instance_list = []
            for key, obj in models.storage.all().items():
                if obj.__class__.__name__ == 'City':
                    if obj.state_id == self.id:
                        instance_list.append(obj)
            return instance_list
