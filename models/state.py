#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String
from models.city import City
import models


class State(BaseModel, Base):
    """ State class """

    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref='state', cascade="all, delete")

    @property
    def cities(self):
        """
        getter attribute cities that returns the list of City instances
        """
        my_list = []
        extract = models.storage.all(City)
        for city in extract.values():
            if city.state_id == self.id:
                my_list.append(city)
        return my_list
