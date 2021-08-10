#!/usr/bin/python3
""" State Module for HBNB project """
import os
import models
from sqlalchemy import Column, String
from models.city import City
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """ State class """
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state",
                              cascade="delete")

    else:
        name = ""

        @property
        def cities(self):
            """
                Getter method that returns list of city 
                instances with state_id == State.id 
                FileStorage Relationship between State and City
            """
            cities_dict = models.storage.all(City)
            city_list = []
            for key, value in cities_dict.items():
                if value.state_id == self.id:
                    city_list.append(v)
            return city_list
