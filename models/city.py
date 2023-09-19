#!/usr/bin/python3
"""This script defines the City class."""
from models.base_model import Base
from models.base_model import BaseModel
from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import relationship

class City(BaseModel, Base):
    """Represents a city in a MySQL database.

    Inherits from SQLAlchemy Base and is linked to the MySQL table 'cities'.

    Attributes:
        __tablename__ (str): The name of the MySQL table for storing cities.
        name (sqlalchemy String): The name of the city.
        state_id (sqlalchemy String): The state ID of the city.
    """
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")

