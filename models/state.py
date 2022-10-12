#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models import storage_type


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    if storage_type == "db":
        @property
        def cities(self):
            '''Return a list of cities with the same state_id
            as current instance
            '''
            from models import storage
            result = [city for city in storage.all(City).values()
                      if city.state_id == self.id]
            return result
