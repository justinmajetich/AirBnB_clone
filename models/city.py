#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ The city class, contains state ID and name
    Attributes:
        __tablename__ (str): Name of the table
        state_id (str): The state id.
        name (str): The name of the city.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

    state = relationship('State', back_populates="cities")
    places = relationship('Place', cascade='all, delete-orphan',
                          back_populates="cities")
