#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, ForeignKey
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

        @property
        def cities(self):
            from models import storage
            result = []
            dict_cities = storage.all("City")
            for key, obj in dict_cities.items():
                if self.id == obj["state_id"]:
                    result.append(obj)
            return result
    else:
        name = ""
