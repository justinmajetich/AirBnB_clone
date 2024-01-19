#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(60), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_MYSQL_DB") != "db":
        @property
        def cities(self):
            """ getter for cities """
            city_list = []
            from models import storage
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
