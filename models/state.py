#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from models.city import City
from sqlalchemy.orm import relationship, backref
from os import getenv
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if getenv('HBNB_TYPE_STORAGE') != 'db':

        @property
        def cities(self):
            """ cities getter
            Returns the list of City instances with
            state_id equals to the current State.id
            """
            from models import storage

            our_cts = storage.all(City)
            state_cts = []
            for city in our_cts.values():
                if self.id == city.state_id:
                    state_cts.append(city)

            return state_cts
    else:
        cities = relationship(
            'City',
            cascade='all, delete-orphan',
            backref='state',
        )
