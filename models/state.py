#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from models.city import City
from models.__init__ import storage


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    @property
    def cities(self):
        '''cities'''
        new_dict = []

        all_city = storage.all(City).items()
        for key, value in all_city:
            if value.to_dict()['state_id'] == self.id:
                new_dict.append(value)
        return new_dict
