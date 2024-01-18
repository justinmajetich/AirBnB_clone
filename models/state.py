#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class State(BaseModel):
    """ 
    The State class, which represents information about states in HBNB project.

    Attributes:
        __tablename__ (str): The table name in the database.
        name (Column): Represents a column containing a string (128 characters).
        cities (relationship): For DBStorage, it represents a relationship with the class City.
                              If the State object is deleted, all linked City objects must be
                              automatically deleted. Also, the reference from a City object to
                              its State should be named state.
    """

    # Table name in the database
    __tablename__ = "states"

    # Represents a column containing a string (128 characters)
    name = Column(String(128), nullable=False)

    # For DBStorage: Represents a relationship with the class City
    # If the State object is deleted, all linked City objects must be automatically deleted.
    # Also, the reference from a City object to its State should be named state.
    cities = relationship("City", backref="state", cascade="all, delete-orphan")
