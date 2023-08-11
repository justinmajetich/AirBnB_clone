#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.sql.schema import Column, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from os import getenv
import models
from sqlalchemy.sql.sqltypes import Strings


if getenv("HBNB_TYPE_STORAGE") == "db":
    class State(BaseModel, Base):
        """ State class """
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state',
                              cascade="all, delete, delete-orphan")
else:
    class State(BaseModel):
        """ State class """
        name = ""


        @property
        def cities(self):
            cities_list = []
            cities = models.storage.all(City).values()
            for city in cities:
                if city.state_id == self.id:
                    cities_list.append(city)
            return cities_list
