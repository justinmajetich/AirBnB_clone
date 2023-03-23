#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

class State(Base, BaseModel):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    
    cities = relationship("city", cascade="all, delete-orphan", backref="state")

    @property
    def cities(self):
        # Return list of City instances with state_id = current State.id

        from models.city import City
        city_list = []
        for city in models.storage.all(City).value():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list

