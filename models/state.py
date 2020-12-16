#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship, backref
from sqlalchemy import Column, Integer, String


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="states",
                          cascade="all, delete-orphan")

    @property
    def cities(self):
        """document"""
        from models import storage
        if getenv("HBNB_TYPE_STORAGE") != 'db':
            """Get a list of all related City objects."""

            cities_list = storage.all(City)
            all_cities = []
            for value in cities_list.items():
                for val in storage.all(State).items():
                    if value.state_id == State.id:
                        all_cities.append(value)
            return all_cities
