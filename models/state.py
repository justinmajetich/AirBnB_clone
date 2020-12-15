#!/usr/bin/python3
""" State class"""
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, String, ForeignKey, Integer
import os
from models.city import City
import models


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
    name: input name
    """
    __tablename__ = "states"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City",
                              cascade="all, delete, delete-orphan",
                              backref="state")
    else:
        @property
        def cities(self):
            """Return list of city"""
            city_list = [value for key, value in
                         models.storage.all(City).items()
                         if value.state_id == self.id]
            return city_list
