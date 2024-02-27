#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


STO_TYP = getenv("HBNB_TYPE_STORAGE")

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
    @property
    def cities(self):
        """attribute getter for FileStorage"""
        city_list = []
        for city in models.storage.all("City").values():
            if city.state.id == self.id:
                city_list.append(city)
        return city_list