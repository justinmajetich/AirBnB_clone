#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel
from models.base_model import Base


class State(BaseModel, Base):
    """ State class """
    name = ""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete-orphan")

    @property
    def cities(self):
        """Getter attribute to return the list of City instances with state_id
        equal to the current State.id for FileStorage."""
        cities = []
        for city in storage.all("City").values():
            if city.state_id == self.id:
                cities.append(city)
        return cities
