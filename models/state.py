#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

    else:
        @property
        def cities(self):
            lista = []
            # Returns the list of City instances with
            # state_id == to the current State.id
            for value in storage.all(City).values():
                dict_obj = v.to_dict()
                if dict_obj["state_id"] == self.id:
                    lista.append(value)
            return (lista)
