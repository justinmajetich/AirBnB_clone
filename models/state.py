#!/usr/bin/python3
""" State module """
from models import storage
from os import getenv
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", cascade="all, delete", backref="state",
                              passive_deletes=True)
    else:
        @property
        def cities(self):
            """Return the list of cities"""
            list_city = []
            for value in storage.all(City).values():
                if value.state_id == self.id:
                    list_city.append(value)
            return list_city
