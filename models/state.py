#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    cities = relationship("City", cascade='all, delete-orphan',
                          backref='state')

    @property
    def cities(self):
        from models.city import City
        from models import storage
        all_cities = storage.all(City).values()

        # Filter cities based on the current state's ID
        filtered_cities = []
        for city in all_cities:
            if city.state_id == self.id:
                filtered_cities.append(city)

        # Return the list of filtered cities
        return filtered_cities
