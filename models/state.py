#!/usr/bin/python3
""" State Module"""
from models.base_model import BaseModel, Base
from os import getenv
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
import models


class State(BaseModel, Base):
    """ State class attribute """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        @property
        def cities(self):
            """return list"""
            new_list = []
            value = models.storage.all(City).values()
            for i in value:
                if self.id == i.state_id:
                    new_list.append(i)
            return new_list
