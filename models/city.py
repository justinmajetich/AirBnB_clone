#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, ForeignKey, String
from models.base_model import BaseModel, Base


class City(BaseModel, Base):
    """
    >>City inherits from BaseModel and Base (respect the order)
    >>class attribute __tablename__ -
            represents the table name, cities
    >>class attribute name
            represents a column containing a string (128 characters)
            cant be null
    >>class attribute state_id
            represents a column containing a string (60 characters)
            cant be null
            is a foreign key to states.id
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
