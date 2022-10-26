#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    storageType = getenv("HBNB_TYPE_STORAGE")
    if storageType == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='State')
    
    @property
    def cities(self):
        """ returns list of City instances with matching state ids"""
        Citylist = []
        for val in storage.all(City).values():
            if val.state_id == self.id:
                Citylist += val
        return Citylist
