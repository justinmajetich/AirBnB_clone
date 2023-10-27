#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.city import city
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = states
    name = Column(string(128), nullable=False)

    if getenv("HBNB_TYPE_STORAGE") == "db":
        citites = relationship, ("City", backref="state", cascade="delete")
    else:
        @property
        def cities(self):
            from models import storage
            city_list = []
            for city in storage.all("City").values():
                if city.state_id == self.id:
                    city_list.append(city)
                    return city_list
