#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """ Represents a city for MySQL database

        Atrributes:
            __tablename__ (str): Name of the MySQL table to store cities
            name (sqlalchemy string): Name of the City
            state_id (sqlalchemy String): The state id of the city
            places (sqlalchemy relationship): The User Place Relationship
    """
    __tablename__ = 'cities'
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
