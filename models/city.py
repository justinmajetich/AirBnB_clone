#!/usr/bin/python3
"""
Define the ``City`` class that inherits from the class ``BaseModel``
"""
from models.base_model import BaseModel
from models.base_model import Base
from models.base_model import (
        Column,
        String,
        ForeignKey,
        relationship
        )


class City(BaseModel, Base):
    """
    Define the class City

    * __tablename__: represents the table name, cities
    * name (String): represents a column containing a string (128 characters)
        * can't be null
    * state_id (String): represents a column containing a string \
(60 characters)
        * can't be null
        * is a foreign key to 'states.id'
    """
    __tablename__ = "cities"

    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)

    # Relationships
    places = relationship("Place", backref="cities",
                          cascade="all, delete, delete-orphan")
