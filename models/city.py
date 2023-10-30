#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Foreignkey


class City(BaseModel):
    """ The city class
    Attributes:
        state_id: state id
        name: name of city
        __tablename__: name of table to store cities
        """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), Foreignkey("states.id"), nullable=False)
