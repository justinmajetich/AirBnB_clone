#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False, default="")
    _cities = relationship("City", backref="state", cascade="all, delete, delete-orphan")
    #does _cities need to be private? 
    # what about the reference from a city object being named "state?"
    #Returns all City instances with matching state_id to the State instance calling this method
    @property
    def cities(self):
        from models import storage
        all_cities = storage.all(BaseModel.City)
        # does storage.all and the following work for both db and filestorage?
        return [city for city in all_cities.values() if city.state_id == self.id]
