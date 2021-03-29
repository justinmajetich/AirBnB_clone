#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
import models


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")
    
    @property
    def cities(self):
        """ this is a temp comment """
        city_list = []
        city_obj = models.storage.all(City)  # gets city objs from storage
        for key, value in city_obj.items():
            if value.state_id == self.id:  # finds citys from current state
                city_list.append(value)
        return city_list  # returns citys in state
