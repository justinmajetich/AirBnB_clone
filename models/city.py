#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name

    Atributes:
        __tablename__: represents the tablename cities
        name: represents a column containing a string (128 characters)
        state_id: represents a column containing a string (60 characters)
                  and a foreign key to states.id"""
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=false)
    name = Column(String(128), nullable=false)
