#!/usr/bin/python3
""" State Module for HBNB project """

from os import getenv
from models import storage
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel):
    """ State class """

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    cities = relationship('City', cascade="delete", backref='state')

    if getenv("HBNB_TYPE_STORAGE") == "file":
        @property
        def cities(self):
            ''' cities getter '''

            ret = []

            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    ret.append(City)

            return ret
