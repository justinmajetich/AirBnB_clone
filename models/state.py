#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """Getter attribute that returns the list of City instances."""
        from models import storage
        city_list = []
        extracted_cities = storage.all(City).values()
        for city in extracted_cities:
            if self.id == city.state_id:
                city_list.append(city)
        return city_list
