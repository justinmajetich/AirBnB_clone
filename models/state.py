#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.storage import all
from models.city import City
from sqlalchemy import Column, String, ForeignKey


class State(BaseModel):
    """ State class """
    __tablename__ 'states'
    name = Column(String(128), nullable=False)
    cities = relationship('City', backref='state', cascade="all, delete-orphan")

    @property
    def cities(self):
        list_cities = []
        for cities in storage.all(City).values():
            if city.state_id == self.id:
                list_cities.append(cities)
        return (list_cities)
