#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models import storage_t, storage
from models.city import City
from sqlalchemy import Column, String


class State(BaseModel, Base):
    """ State class """
    if storage_t == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state')
    else:
        name = ""

        @property
        def cities(self):
            my_list = [city for city in storage.all(City).values()
                       if city.state_id == self.id]
            return my_list
