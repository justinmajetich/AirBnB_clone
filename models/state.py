#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City

from sqlalchemy import MetaData, Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state',
                          cascade="all, delete, delete-orphan")

    @property
    def cities(self):
        """ cities getter for fileStorage option
        Returns all cities whose state_id == current state's id (self.id) """
        # get all City objects and filter w.r.t state_id
        from models import storage
        all_cities = storage.all(City)  # returns a dict of objects
        state_cities = {}
        if all_cities:
            for key, val in all_cities.items():
                if self.id in val:
                    state_cities[key] = val
        return state_cities  # a dict of City objects in this state
