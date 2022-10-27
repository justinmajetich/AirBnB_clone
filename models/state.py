#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    storageType = getenv("HBNB_TYPE_STORAGE")
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if storageType == 'db':
        cities = relationship('City',
                              cascade="all, delete-orphan",
                              backref='state'
                              )

    elif storageType == 'file':
        @property
        def cities(self):
            """ returns list of City instances with matching state ids"""
            from models import storage

            Citylist = []
            for val in storage.all(City).values():
                if val.state_id == self.id:
                    Citylist.append(val)
            return Citylist
