#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
import models


class State(BaseModel):
    """ State class """
     __tablename__ = "states"
    name = Column(String(128) nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        """returns the list of City instances with
        state_id equals to the current State.id"""
        city_list = []
        for city in  models.storage.all("City").values():
            if city.state_id = self.id:
                city_list.append(city)
        return city_list

