#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    #Creates a 2-way link where you can access the city by (State)instance.cities and the other way
    #by (City)instance.state. Also, cascade will delete all cities if its parent state is deleted
    cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")

    #Returns all City instances with matching state_id to the State instance calling this method
    def cities(self):
        from models import storage
        all_cities = storage.all(BaseModel.City)
        return [city for city in all_cities.values() if city.state_id == self.id]
