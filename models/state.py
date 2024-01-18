#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models import storage
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    # for DBStorage: Define Cities relationship
    cities = relationship(
            "City",
            backref="state",
            cascade="all, delete-orphan")

    # For FileStorage: define Cities getter
    @property
    def cities(self):
        """Return the list of City instances with state_id
        which equals the current State.id
        """
        all_cities = storage.all("City")
        city_list = []
        for cities in all_cities.values():
            if cities.state_id == self.id:
                city_list.append(cities)
        return city_list
