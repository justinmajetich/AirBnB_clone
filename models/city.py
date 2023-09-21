#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Represents a city for a database.
    Inherits:
        BaseModel
        Base
    Attributes:
        __tablename__: the table name in the database.
        places: places in the city, relationship with city
        name: name of the city.
        state_id: state ID of the city foreign key
    """
    __tablename__ = "cities"
    places = relationship("Place", backref="cities",
                          cascade="all, delete-orphan")
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
