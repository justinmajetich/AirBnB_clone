#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.engine import Filestorage
from models.city import City
from sqlalchemy Column, String, Integer
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ The State class """
    __tablename__ = "states"
    name = Column(String(128) nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            return [obj for obj
                    in Filestorage.all(City).values()
                    if obj.state_id == self.id]
