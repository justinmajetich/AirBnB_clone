#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import Base, BaseModel
import models
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """State class."""
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship('City', backref='state', cascade='delete')

    @property
    def cities(self):
        """Return the list of City instances with state_id equals
        to the current State.id."""
        cities = []
        for obj in models.storage.all(City).items():
            if obj.state_id == self.id:
                cities.append(obj)
        return cities
