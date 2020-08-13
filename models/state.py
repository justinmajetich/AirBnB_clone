#!/usr/bin/python3
""" State Module for HBNB project """

from os import getenv
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)

    cities = relationship('City', cascade="all, delete", backref='state')


    @property
    def cities(self):
        ''' cities getter '''
        from models.engine import FileStorage

        for n, city in FileStorage.__objects.items():
            if city.state_id == self.id:
                ret.append(City)

        return ret
