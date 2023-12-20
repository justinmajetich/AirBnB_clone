#!/usr/bin/python3
""" State Module for HBNB project """
import models
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel, Base
from os import getenv
from models.city import City
from models.place import Place
from sqlalchemy import Integer, String, Column, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class definition """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            """Getter for cities"""
            from models import storage
            return [ct for ct in storage.all(City).values()
                    if ct.state_id == self.id]
