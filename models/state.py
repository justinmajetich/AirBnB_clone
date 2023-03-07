#!/usr/bin/python3
"""State module for HBNB project."""
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """State class for storing state information."""

    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        @property
        def cities(self):
            """getter method that returns the list of City instances with state_id equals to the current State.id"""
            from models import storage
            list_cities = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    list_cities.append(city)
            return list_cities

    def __init__(self, *args, **kwargs):
        """Initializes State."""
        if os.getenv("HBNB_TYPE_STORAGE") != "db":
            self.name = ""
        super().__init__(*args, **kwargs)