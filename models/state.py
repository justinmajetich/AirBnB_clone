#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from models.city import City
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(length=128), nullable=False)
        cities = relationship("City",
                              backref='state',
                              cascade="all, delete-orphan")
    else:
        name = ""

        @property
        def cities(self):
            """ getter to cities asociated with the current state """
            from models import storage
            cities = []
            objects = storage.all("City")
            for obj in objects.values():
                if City == type(obj) and obj.state_id == self.id:
                    cities.append(obj)
            return obj
