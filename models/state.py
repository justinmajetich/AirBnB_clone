#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """ State class """

    __tablename__ = "states"

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")

    else:
        name = ""

        @property
        def cities(self):
            """ getter to filestorage """
            lista = []
            # Returns the list of City instances with
            # state_id == to the current State.id
            for value in storage.all(City).values():
                dict_obj = value.to_dict()
                if dict_obj["state_id"] == self.id:
                    lista.append(value)
            return (lista)
