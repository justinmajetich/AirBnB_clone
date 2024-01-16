#!/usr/bin/python3
""" State Module for Airbnb project """
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"

    name = Column(String(128), nullable=False)
    
    # For DBStorage
    cities = relationship('City', backref='state', cascade='all, delete-orphan')

    # For FileStorage
    @property
    def cities(self):
        """ Getter attribute that returns the list of City instances """
        from models import storage
        return [city for city in storage.all(City).values() if city.state_id == self.id]
