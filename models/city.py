#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """
        Represents a city in the database.

        Attributes:
            __tablename__ (string): The name of the table.
            state_id (sqlalchemy string): The state_id of a state.
            name(sqlalchemy string): The name of the city.
    """
    __tablename__ = "cities"
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    name = Column(String(128), nullable=False)

    places = relationship('Place', backref='cities', cascade="all, delete-orphan")