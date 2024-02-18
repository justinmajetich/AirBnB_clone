#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    
    # For DBStorage
    cities = relationship("City", backref="state", cascade="all, delete")

    # For FileStorage
    @property
    def cities(self):
        """
        Getter attribute to return a list of City instances with
        state_id equal to the current State.id
        """
        from models import storage
        city_instances = storage.all(City)
        for city in city_instances.values():
            if city.state_id == self.id:
                return city

    # name = ""
