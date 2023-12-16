#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models import city
import os

class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete-orphan")
    else:
       @property
       def cities(self):
            """
            Getter attribute that returns the list of City instances
            with state_id equals to the current State.id.
            """
            from models import storage
            city_list = storage.all(city.City).values()
            return [city for city in city_list if city.state_id == self.id]