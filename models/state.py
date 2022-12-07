#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String
from sqlalchemy.orm import backref, relationship
from sqlalchemy.sql.schema import Column
from os import getenv

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref("state"), cascade="delete")


    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
                """returns list of City instances with state_id = State.id"""
                from models import storage
                related_cities = []
                for city in list(models.storage.all(City).values()):
                        if city.state_id == self.id:
                                related_cities.append(city)
                return related_cities
