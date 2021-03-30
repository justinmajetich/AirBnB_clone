#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import environ


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    

    if environ.getenv("HBNB_TYPE_STORAGE") == 'db':
        cities = relationship('City', cascade="all, delete", backref='state')
    else:
        @property
        def cities(self):
            ''' getter for FileStorage cities-state '''
            from models import storage
            load = []
            for value in storage.all(City).items():
                if self.state_id == value.id:
                    load.append(value)
            return load
