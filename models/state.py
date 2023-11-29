#!/usr/bin/python3
from models.base_model import BaseModel
<<<<<<< HEAD
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv
import models
from models.city import City


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    if getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City", backref="state",
                              cascade="all, delete, delete-orphan")
    else:

        @property
        def cities(self):
            """Getter attribute cities that returns the list of City instances"""
            city_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
=======
"""
Module class: State
"""


class State(BaseModel):
    """definition for class State"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ constructor method """
        super().__init__(self, *args, **kwargs)
>>>>>>> master
