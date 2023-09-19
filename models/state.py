#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cascade = "all, delete-orphan"
    """When a state oblect is deleted, all lonked City objects are deleted"""
    cities = relationship("City", backref="state", cascade=cascade)

    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances"""
        city_instances = storage.all("City").values()
        return [city for city in city_instances if city.state.id == self.id]
