#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """Represents a city for a database.

    Inherits from SQLAlchemy Base and links to the MySQL table cities.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store cities.
        places (sqlalchemy relationship): The places in the city.
        name (sqlalchemy String): The name of the city.
        state_id (sqlalchemy String): The state ID of the city.
    """
    __tablename__ = "cities"
    places = relationship("Place", backref="cities", cascade="all, delete-orphan")
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)

