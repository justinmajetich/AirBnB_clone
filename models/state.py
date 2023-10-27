#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    #if not db storage? FIX THIS!!!
    @property
    def cities(self):
        list_of_cities = []
        for object in models.storage.all(City).values():
            if object.state_id == self.id:
                list_of_cities.append(object)
        return object
