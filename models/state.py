#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """

    if models.typestorage == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        # If State object is deleted, all linked City objects auto deleted
        cities = relationship("City", backref="state")
    else:
        name = ""

    if models.typestorage != "db":
        @property
        def cities(self):
            """
            Getter attribute to list City instaces
            """
            new_list = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    new_list.append(city)
            return new_list
