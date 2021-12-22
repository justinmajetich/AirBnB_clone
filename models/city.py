#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey


""" Inherits from base (respecting order) """
class City(BaseModel, Base):
    """ The city class, contains state ID and name

    Class Attributes:
    __tablename__: represents the table name, cities
    name: represents a column containing a string (128 chars)
    state_id: represents a column containing a string (60 chars)
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), nullable=False, ForeignKey("states.id"))
