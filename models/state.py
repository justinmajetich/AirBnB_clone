#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade="all, delete", backref='state')

    if environ.get("HBNB_TYPE_STORAGE") != 'db':
        @property
        def cities(self):
            ''' getter for FileStorage cities-state '''
            from models import storage
            l = []
            for v in storage.all(City).values():
                if v.state_id == self.id:
                    l.append(v)
            return l
