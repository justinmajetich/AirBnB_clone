#!/usr/bin/python3
"""
 State Module for HBNB project
 This module defines the State class, a subclass of BaseModel and Base.
 Attributes:
     __tablename__ (str): The name of the MySQL table to store states.
     name (sqlalchemy.Column): The name of the state, represented as a
     string of up to 128 characters.
     cities (sqlalchemy.orm.relationship or property):
     Represents a relationship
     If a State object is deleted all linked City objects are automatically
     deleted as well.
     If the storage type is not 'db', this attribute is a property that returns
     a list of City instances with state_id equal to the current State.id.
"""
import os

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel
from models.city import City

storage_type = os.getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"

    if storage_type == "db":
        name = Column(String(128), nullable=False)
        cities = relationship(
                "City",
                backref="state",
                cascade="all, delete-orphan"
                )
    else:
        name = ""

    if storage_type != "db":
        @property
        def cities(self):
            """
            Returns the list of City instances with
            state_id equals to the current State.id
            """
            from models import storage

            all_cities = storage.all(City)
            return [
                    city for city in all_cities.values()
                    if city.state_id == self.id
                    ]
